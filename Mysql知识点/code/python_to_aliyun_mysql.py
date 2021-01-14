from sshtunnel import SSHTunnelForwarder
import pymysql

# 通过SSH连接云服务器
server = SSHTunnelForwarder(
	ssh_address_or_host=("ip", 22),  # 云服务器地址IP和端口port
	ssh_username="admin",  # 云服务器登录账号admin
	ssh_password="passwd",  # 云服务器登录密码password
	remote_bind_address=('localhost', 3306)  # 数据库服务地址ip,一般为localhost和端口port，一般为330
)

# 云服务器开启
server.start()
# 云服务器上mysql数据库连接
con = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                      port=server.local_bind_port,
                      user="summer",  # mysql的登录账号admin
                      password="summer",  # mysql的登录密码pwd
                      db="jing_dong",  # mysql中要访问的数据表
                      charset='utf8')  # 表的字符集
# 创建游标
cur = con.cursor()
# 执行sql语句
cur.execute("""SELECT * from goods where id>4""")
# 读取数据
data = cur.fetchall()
# 打印数据
for item in data:
	print(item)
# 游标、连接关闭
cur.close()
con.close()
# 云服务器关闭
server.close()
