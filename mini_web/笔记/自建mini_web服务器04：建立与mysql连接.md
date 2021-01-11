# 自建Mini_Web服务器（4）：建立与mysql连接

[传送门](https://github.com/Jsummer121/Mini-Web-Server)

## 一、回顾

&nbsp;&nbsp;&nbsp;&nbsp;之前我们用socket写了一个服务器，能够让浏览器访问资源，后来我们将动态资源剥离开来，再然后我们引入了路由功能，现在我们将使用我们的mysql使得整个网页活起来。

## 二、数据准备

### 2.1 创建数据库

```sql
create database stock_db charset=utf8;
```

### 2.2 选择数据库

```sql
use stock_db
```

### 2.3 导入数据

```sql
source stock_db.sql
```

### 2.4 表结构如下：

```sql
mysql> desc focus;
+-----------+------------------+------+-----+---------+----------------+
| Field     | Type             | Null | Key | Default | Extra          |
+-----------+------------------+------+-----+---------+----------------+
| id        | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| note_info | varchar(200)     | YES  |     |         |                |
| info_id   | int(10) unsigned | YES  | MUL | NULL    |                |
+-----------+------------------+------+-----+---------+----------------+
mysql> desc info;
+----------+------------------+------+-----+---------+----------------+
| Field    | Type             | Null | Key | Default | Extra          |
+----------+------------------+------+-----+---------+----------------+
| id       | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| code     | varchar(6)       | NO   |     | NULL    |                |
| short    | varchar(10)      | NO   |     | NULL    |                |
| chg      | varchar(10)      | NO   |     | NULL    |                |
| turnover | varchar(255)     | NO   |     | NULL    |                |
| price    | decimal(10,2)    | NO   |     | NULL    |                |
| highs    | decimal(10,2)    | NO   |     | NULL    |                |
| time     | date             | YES  |     | NULL    |                |
+----------+------------------+------+-----+---------+----------------+
```

## 三、从mysql中查询数据

我们可以看一下index.html文件。发现我们只需要将数据读取出来之后，按照个数一次递归然后将每个值依次放入`<tr><td>`即可。

```html
      <table class="table table-hover">
        <tr>
            <th>序号</th>
            <th>股票代码</th>
            <th>股票简称</th>
            <th>涨跌幅</th>
            <th>换手率</th>
            <th>最新价(元)</th>
            <th>前期高点</th>
            <th>前期高点日期</th>
            <th>添加自选</th>
        </tr>
        {%content%}       
      </table>
```

那我们需要的顺序如下：

-   连接数据库
-   获取游标对象
-   执行sql语句
-   获取返回值，然后依次递归
-   将值依次放入对应位置即可

```python
@route("/index.html")
def index():
    with open("./templates/index.html") as f:
        content = f.read()

    # 创建Connection连接
    conn = connect(
        host='localhost',
        port=3306,
        user='user',
        password='password',
        database='stock_db',
        charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()
    cs.execute("select * from info;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()

    tr_template = """<tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007">
        </td>
        </tr>
    """

    html = ""
    for line_info in stock_infos:
        html += tr_template % (line_info[0],
                               line_info[1],
                               line_info[2],
                               line_info[3],
                               line_info[4],
                               line_info[5],
                               line_info[6],
                               line_info[7])

    content = re.sub(r"\{%content%\}", html, content)

    return content
```

按照这个步骤，我们就可以将center函数也补充完整：

```python
@route("/center.html")
def center():
    with open("./templates/center.html") as f:
        content = f.read()

    # 创建Connection连接
    conn = connect(
        host='localhost',
        port=3306,
        user='root',
        password='summer',
        database='stock_db',
        charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()
    cs.execute(
        "select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i inner join focus as f on i.id=f.info_id;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()

    tr_template = """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <a type="button" class="btn btn-default btn-xs" href="/update/300268.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
            </td>
            <td>
                <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="300268">
            </td>
        </tr>
    """

    html = ""
    for line_info in stock_infos:
        html += tr_template % (line_info[0],
                               line_info[1],
                               line_info[2],
                               line_info[3],
                               line_info[4],
                               line_info[5],
                               line_info[6])

    # content = re.sub(r"\{%content%\}", str(stock_infos), content)
    content = re.sub(r"\{%content%\}", html, content)

    return content

```

## 四、实现增删改

### 4.1 Mysql增

增的按钮放在index.html中。为了实现增加需要使用js在按钮上添加操作

```javascript
<script>
        $(document).ready(function(){

                $("input[name='toAdd']").each(function(){  
                    var currentAdd = $(this);  
                    currentAdd.click(function(){  
                        code = $(this).attr("systemIdVaule"); 
                        // alert("/add/" + code + ".html"); 
                        $.get("/add/" + code + ".html", function(data, status){
                            alert("数据: " + data + "\n状态: " + status);
                        });
                    });  
                });  
        });
</script>
```

此时，只需要在按照正则匹配路由的方式写入即可。

```python
@route(r"/add/(\d+)\.html")
def add_focus(ret):
    # 1. 获取股票代码
    stock_code = ret.group(1)

    # 2. 判断试下是否有这个股票代码
    conn = connect(
        host='localhost',
        port=3306,
        user='root',
        password='summer',
        database='stock_db',
        charset='utf8')
    cs = conn.cursor()
    sql = """select * from info where code=%s;"""
    cs.execute(sql, (stock_code,))
    # 如果要是没有这个股票代码，那么就认为是非法的请求
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "没有这支股票，大哥 ，我们是创业公司，请手下留情"

    # 3. 判断以下是否已经关注过
    sql = """ select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;"""
    cs.execute(sql, (stock_code,))
    # 如果查出来了，那么表示已经关注过
    if cs.fetchone():
        cs.close()
        conn.close()
        return "已经关注过了，请勿重复关注"

    # 4. 添加关注
    sql = """insert into focus (info_id) select id from info where code=%s;"""
    cs.execute(sql, (stock_code,))
    conn.commit()
    cs.close()
    conn.close()

    return "关注成功"

```

### 4.2 Mysql 删

删的操作在center.html中，同样的需要添加一个js操作

```javascript
<script>
        $(document).ready(function(){

                $("input[name='toDel']").each(function(){  
                    var currentAdd = $(this);  
                    currentAdd.click(function(){  
                        code = $(this).attr("systemIdVaule"); 
                        // alert("/del/" + code + ".html"); 
                        $.get("/del/" + code + ".html", function(data, status){
                            alert("数据: " + data + "\n状态: " + status);
                        });
                        window.location.reload()
                    });  
                });  
        });
</script>
```

此时，按照同样的正则匹配方式：

```python
@route(r"/del/(\d+)\.html")
def del_focus(ret):
    # 1. 获取股票代码
    stock_code = ret.group(1)

    # 2. 判断试下是否有这个股票代码
    conn = connect(
        host='localhost',
        port=3306,
        user='root',
        password='summer',
        database='stock_db',
        charset='utf8')
    cs = conn.cursor()
    sql = """select * from info where code=%s;"""
    cs.execute(sql, (stock_code,))
    # 如果要是没有这个股票代码，那么就认为是非法的请求
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "没有这支股票，大哥 ，我们是创业公司，请手下留情"

    # 3. 判断以下是否已经关注过
    sql = """ select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;"""
    cs.execute(sql, (stock_code,))
    # 如果没有关注过，那么表示非法的请求
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "%s 之前未关注，请勿取消关注" % stock_code

    # 4. 取消关注
    # sql = """insert into focus (info_id) select id from info where code=%s;"""
    sql = """delete from focus where info_id = (select id from info where code=%s);"""
    cs.execute(sql, (stock_code,))
    conn.commit()
    cs.close()
    conn.close()

    return "取消关注成功"

```

### 4.3 Mysql改

改直接在按钮上添加了`a`标签，因此直接可以请求相应的函数然后返回值，在修改完之后请求另一个修改函数即可。

```python
@route(r"/update/(\d+)\.html")
def show_update_page(ret):
    """显示修改的那个页面"""
    # 1. 获取股票代码
    stock_code = ret.group(1)

    # 2. 打开模板
    with open("./templates/update.html") as f:
        content = f.read()

    # 3. 根据股票代码查询相关的备注信息
    conn = connect(
        host='localhost',
        port=3306,
        user='root',
        password='summer',
        database='stock_db',
        charset='utf8')
    cs = conn.cursor()
    sql = """select f.note_info from focus as f inner join info as i on i.id=f.info_id where i.code=%s;"""
    cs.execute(sql, (stock_code,))
    stock_infos = cs.fetchone()
    note_info = stock_infos[0]  # 获取这个股票对应的备注信息
    cs.close()
    conn.close()

    content = re.sub(r"\{%note_info%\}", note_info, content)
    content = re.sub(r"\{%code%\}", stock_code, content)

    return content

```

提交修改信息

```python
@route(r"/update/(\d+)/(.*)\.html")
def save_update_page(ret):
    """"保存修改的信息"""
    stock_code = ret.group(1)
    comment = ret.group(2)
    comment = urllib.parse.unquote(comment)

    conn = connect(
        host='localhost',
        port=3306,
        user='root',
        password='summer',
        database='stock_db',
        charset='utf8')
    cs = conn.cursor()
    sql = """update focus set note_info=%s where info_id = (select id from info where code=%s);"""
    cs.execute(sql, (comment, stock_code))
    conn.commit()
    cs.close()
    conn.close()

    return "修改成功"
```

## 五、整个mini_frame.py

```python
import re
import urllib.parse
from pymysql import connect

"""
URL_FUNC_DICT = {
    "/index.html": index,
    "/center.html": center
}
"""

URL_FUNC_DICT = dict()


def route(url):
    def set_func(func):
        # URL_FUNC_DICT["/index.py"] = index
        URL_FUNC_DICT[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)

        return call_func

    return set_func


@route(r"/index.html")
def index(ret):
    with open("./templates/index.html") as f:
        content = f.read()

    # 创建Connection连接
    conn = connect(
        host='localhost',
        port=3306,
        user='root',
        password='summer',
        database='stock_db',
        charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()
    cs.execute("select * from info;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()

    tr_template = """
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
        </td>
    </tr>
    """

    html = ""
    for line_info in stock_infos:
        html += tr_template % (line_info[0],
                               line_info[1],
                               line_info[2],
                               line_info[3],
                               line_info[4],
                               line_info[5],
                               line_info[6],
                               line_info[7],
                               line_info[1])

    content = re.sub(r"\{%content%\}", html, content)

    return content


@route(r"/center.html")
def center(ret):
    with open("./templates/center.html") as f:
        content = f.read()

    # my_stock_info = "这里是从mysql查询出来的数据。。。"
    # content = re.sub(r"\{%content%\}", my_stock_info, content)
    # 创建Connection连接
    conn = connect(
        host='localhost',
        port=3306,
        user='root',
        password='summer',
        database='stock_db',
        charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()
    cs.execute(
        "select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i inner join focus as f on i.id=f.info_id;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()

    tr_template = """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
            </td>
            <td>
                <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
            </td>
        </tr>
    """

    html = ""
    for line_info in stock_infos:
        html += tr_template % (line_info[0],
                               line_info[1],
                               line_info[2],
                               line_info[3],
                               line_info[4],
                               line_info[5],
                               line_info[6],
                               line_info[0],
                               line_info[0])

    content = re.sub(r"\{%content%\}", html, content)

    return content


# 给路由添加正则表达式的原因：在实际开发时，url中往往会带有很多参数，例如/add/000007.html中000007就是参数，
# 如果没有正则的话，那么就需要编写N次@route来进行添加 url对应的函数 到字典中，此时字典中的键值对有N个，浪费空间
# 而采用了正则的话，那么只要编写1次@route就可以完成多个 url例如/add/00007.html
# /add/000036.html等对应同一个函数，此时字典中的键值对个数会少很多
@route(r"/add/(\d+)\.html")
def add_focus(ret):
    # 1. 获取股票代码
    stock_code = ret.group(1)

    # 2. 判断试下是否有这个股票代码
    conn = connect(
        host='localhost',
        port=3306,
        user='root',
        password='summer',
        database='stock_db',
        charset='utf8')
    cs = conn.cursor()
    sql = """select * from info where code=%s;"""
    cs.execute(sql, (stock_code,))
    # 如果要是没有这个股票代码，那么就认为是非法的请求
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "没有这支股票，大哥 ，我们是创业公司，请手下留情..."

    # 3. 判断以下是否已经关注过
    sql = """ select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;"""
    cs.execute(sql, (stock_code,))
    # 如果查出来了，那么表示已经关注过
    if cs.fetchone():
        cs.close()
        conn.close()
        return "已经关注过了，请勿重复关注"

    # 4. 添加关注
    sql = """insert into focus (info_id) select id from info where code=%s;"""
    cs.execute(sql, (stock_code,))
    conn.commit()
    cs.close()
    conn.close()

    return "关注成功"


@route(r"/del/(\d+)\.html")
def del_focus(ret):
    # 1. 获取股票代码
    stock_code = ret.group(1)

    # 2. 判断试下是否有这个股票代码
    conn = connect(
        host='localhost',
        port=3306,
        user='root',
        password='summer',
        database='stock_db',
        charset='utf8')
    cs = conn.cursor()
    sql = """select * from info where code=%s;"""
    cs.execute(sql, (stock_code,))
    # 如果要是没有这个股票代码，那么就认为是非法的请求
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "没有这支股票，大哥 ，我们是创业公司，请手下留情"

    # 3. 判断以下是否已经关注过
    sql = """ select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;"""
    cs.execute(sql, (stock_code,))
    # 如果没有关注过，那么表示非法的请求
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "%s 之前未关注，请勿取消关注" % stock_code

    # 4. 取消关注
    # sql = """insert into focus (info_id) select id from info where code=%s;"""
    sql = """delete from focus where info_id = (select id from info where code=%s);"""
    cs.execute(sql, (stock_code,))
    conn.commit()
    cs.close()
    conn.close()

    return "取消关注成功"


@route(r"/update/(\d+)\.html")
def show_update_page(ret):
    """显示修改的那个页面"""
    # 1. 获取股票代码
    stock_code = ret.group(1)

    # 2. 打开模板
    with open("./templates/update.html") as f:
        content = f.read()

    # 3. 根据股票代码查询相关的备注信息
    conn = connect(
        host='localhost',
        port=3306,
        user='root',
        password='summer',
        database='stock_db',
        charset='utf8')
    cs = conn.cursor()
    sql = """select f.note_info from focus as f inner join info as i on i.id=f.info_id where i.code=%s;"""
    cs.execute(sql, (stock_code,))
    stock_infos = cs.fetchone()
    note_info = stock_infos[0]  # 获取这个股票对应的备注信息
    cs.close()
    conn.close()

    content = re.sub(r"\{%note_info%\}", note_info, content)
    content = re.sub(r"\{%code%\}", stock_code, content)

    return content


@route(r"/update/(\d+)/(.*)\.html")
def save_update_page(ret):
    """"保存修改的信息"""
    stock_code = ret.group(1)
    comment = ret.group(2)
    comment = urllib.parse.unquote(comment)

    conn = connect(
        host='localhost',
        port=3306,
        user='root',
        password='summer',
        database='stock_db',
        charset='utf8')
    cs = conn.cursor()
    sql = """update focus set note_info=%s where info_id = (select id from info where code=%s);"""
    cs.execute(sql, (comment, stock_code))
    conn.commit()
    cs.close()
    conn.close()

    return "修改成功"


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    file_name = env['PATH_INFO']
    # file_name = "/index.py"
    try:
        # func = URL_FUNC_DICT[file_name]
        # return func()
        # return URL_FUNC_DICT[file_name]()
        for url, func in URL_FUNC_DICT.items():
            # {
            #   r"/index.html":index,
            #   r"/center.html":center,
            #   r"/add/\d+\.html":add_focus
            # }
            ret = re.match(url, file_name)
            if ret:
                return func(ret)
        else:
            return "请求的url(%s)没有对应的函数" % file_name

    except Exception as ret:
        return "产生了异常：%s" % str(ret)

```



