# Python操作Elasticsearch

## 一、下载

ES下载有许多方式，例如win和linux，docker的es下载看这篇：[传送门](https://blog.csdn.net/jiangSummer/article/details/113816000)

## 二、创建连接

### 1. 指定连接

```python
# -*- coding: utf-8 -*-
# @Auther:Summer
from elasticsearch import Elasticsearch


## 指定连接
es = Elasticsearch(
    ['127.0.0.1:9200'],
    # 认证信息
    # http_auth=('elastic', 'changeme')
)
```

### 2. 动态连接

```python
# -*- coding: utf-8 -*-
# @Auther:Summer
from elasticsearch import Elasticsearch


## 动态连接
es = Elasticsearch(
    ['esnode1:port', 'esnode2:port'],
    # 在做任何操作之前，先进行嗅探
    sniff_on_start=True,
    # 节点没有响应时，进行刷新，重新连接
    sniff_on_connection_fail=True,
    # 每 60 秒刷新一次
    sniffer_timeout=60
)
```

## 三、_cat的使用

```python
# -*- coding: utf-8 -*-
# @Auther:Summer
from elasticsearch import Elasticsearch


es = Elasticsearch(["127.0.0.1:9200"])

# 查看健康状况
print(es.cat.health())
# 结果： 1613725331 09:02:11 elasticsearch yellow 1 1 8 8 0 0 2 0 - 80.0%

# 查看所有索引
print(es.cat.indices())

# 查看所有节点
print(es.cat.nodes())
# 127.0.0.1 33 95 3 0.00 0.00 0.00 cdhilmrstw * 2df5b3cb139d

# 查看主节点
print(es.cat.master())
# ZEFpNCg7T3mM19HZX6rgbQ 127.0.0.1 127.0.0.1 2df5b3cb139d
```

## 四、查询操作

### 1. 查询全部：match_all

```python
from elasticsearch import Elasticsearch

es = Elasticsearch(['127.0.0.1:9200'])

# 查询全部文档
body = {
	"query": {
		"match_all": {}
	}
}

# 执行检索功能
response = es.search(index="newbank", body=body)
# 打印检索返回信息
print(response)
```

### 2. 精准检索：match

索引条件：account_number为20的人

注意，因为查询的时候，主要是进行body部分的修改，因此其余部分省略了。

```python
# 精确检索
body = {
	"query": {
		"match": {
			"account_number": "20"
		}
	}
}
```

### 3. 全文检索：match

索引条件：地址中包含mill的人

```python
# 全文检索
body = {
  "query": {
    "match": {
      "address": "mill"
    }
  }
}
```

精准检索与全文检索的区别在于，精准检索一般是进行一些非text字段的查找，而全文检索则是用于查找text字段。

### 4. 短语匹配：match_phrase

索引条件：地址中包含mill road的人

```python
# 短语匹配
body = {
  "query": {
    "match_phrase": {
      "address": "mill road"
    }
  }
}
```

短语匹配于其他的配的区别在于，短语匹配不会对需要匹配的词语进行分词，而是使用一整个进行匹配。

### 5. 多字段匹配：multi_match

索引条件：地址或者城市中包含mill的所有人

```
# 多字段匹配
body = {
  "query": {
    "multi_match": {
      "query": "mill",
      "fields": ["address","city"]
    }
  }
}
```

### 6. 复合查询：bool

bool有三种方式：must（必须），should（可以满足也可以不满足），must_not（必须不满足）

#### 6-1 must

索引条件：地址包含mill并且是男性的所有人

```python
# 复合查询
## must
body = {
  "query": {
    "bool": {
      "must": [
        {"match": {
          "address": "mill"
        }},
        {"match": {
            "gender": "M"
          }}
      ]
    }
  }
}
```

#### 6-2 must_not

索引条件：地址包含mill并且年龄不是38的所有男性

```python
## must_not
body = {
  "query": {
    "bool": {
      "must": [
        {"match": {
          "address": "mill"
        }},
        {"match": {
            "gender": "M"
          }}
      ],
      "must_not": [
        {"match": {
          "age": "38"
        }}
      ]
    }
  }
}
```

#### 6-3 should

查询条件：查找地址中包含mill的年龄是不是38都行的所有男性

```python
## should
body = {
  "query": {
    "bool": {
      "must": [
        {"match": {
          "address": "mill"
        }},
        {"match": {
            "gender": "M"
          }}
      ],
      "should": [
        {"match": {
          "age": "38"
        }}
      ]
    }
  }
}
```

### 7. 结果过滤：filter

这个条件并不会进行分值的评定。

索引条件：查询工资位于20000到30000的所有人

```python
# filter
body = {
  "query": {
    "bool": {
      "filter": {
        "range": {
          "balance": {
            "gte": 20000,
            "lte": 30000
          }
        }
      }
    }
  }
}
```

### 8. 等于查询

term支持查询某个字段等于某个值这样的业务场景，而terms支持擦互相你某个字段等于多个值的场景

#### 8-1 term

```python
# term
body = {
  "query": {
    "term": {
      "balance": {
        "value": "32838"
      }
    }
  }
}
```

#### 8-2 terms

索引条件：查询firstname为Nanette或Forbes的人

```python
# terms
body = {
  "query": {
    "terms": {
      "firstname": [
        "Nanette",
        "Forbes"
      ]
    }
  }
}
```

### 9. 执行聚合：aggregations

索引条件：查出所有的年龄分布，并且这些年龄段中M的平均薪资和F的平均薪资，以及这个年龄段总体的平均薪资

```python
body = {
  "query": {
    "match_all": {}
  },
  "aggs": {
    "aggAgg": {
      "terms": {
        "field": "age",
        "size": 100
      },
      "aggs": {
        "genderAgg": {
          "terms": {
            "field": "gender.keyword",
            "size": 10
          },
          "aggs": {
            "balanceAvg": {
              "avg": {
                "field": "balance"
              }
            }
          }
        },
        "ageBananceAvg":{
          "avg": {
            "field": "balance"
          }
        }
      }
    }
  },
  "size": 0
}
```

### 10.切片式查询

form从第几条开始，size为查询的数据量

索引条件：查询从第10条开始的5条数据

```python
body = {
  "query": {
    "match_all": {}
  }
  , "from": 10
  , "size": 5
}
```

### 11.排序：sort

索引条件：按照年龄降序查询所有的人

降序：desc。升序：asc（默认）

```python
body = {
  "query": {
    "match_all": {}
  }
  , "sort":{
      "age": {
        "order": "desc"
      }
   }
}
```

如果需要对多个进行排序，可以使用列表。

索引条件：先对年龄进行升序，然后对收入进行降序

```python
{
  "query": {
    "match_all": {}
  }
  , "sort": [
    {
      "age": {
        "order": "desc"
      }
    },{
      "account_number": {
        "order": "asc"
      }
    }
  ]
}
```

## 五、索引

### 1. 创建索引

```python
# 创建索引
es.indices.create("index_name")
```

如果需要自定义mapping，则需要将mapping定义好后传递给body参数即可。

```python
es.indices.create("index_name", body = mapping)
```

### 2. 删除索引

```python
es.indices.delete("index_name")
```

### 3. 重建索引

因为ES不支持修改索引中的mapping，因此，如果想修改的话就只能进行重建，然后将原本的数据进行传入。其中，source_index为原索引，target_index为新的索引。

```python
from elasticsearch import helpers

body = {"query": {"match_all": {}}}
helpers.reindex(client=es,
                source_index="old_index_name",
                target_index="new_index_name",
                target_client=es,
                query=body)
```

### 4. 查看索引

```python
# 查看所有索引
indexs = es.indices.get("*")

# 查看es中索引的索引名
index_name = indexs.keys()

# 查看某个索引
index = es.indices.get("index_name")
```

### 5. 判断某个索引是否存在

```python
# 判断某个索引是否存在
es.indices.exists("index_name")
```

## 六、删除操作

先根据查询语句查询数据，然后使用delete_by_query删除查到的数据

例如：删除地址包含mill的数据

```python
body = {
	"query": {
		"match": {
			"address": "mill"
		}
	}
}
es.delete_by_query(index="newbank", body=body)
```

或者使用delete方法，指定标识符删除

```python
# 指定标识符删除
es.delete(index="newbank", id="pre_val")
```

## 七、映射

### 1. 查看映射

```python
from elasticsearch import Elasticsearch

es = Elasticsearch(["127.0.0.1:9200"])

# 查看索引的映射
response = es.indices.get_mapping(index="newbank")

print(response)
```

### 2. 查看某个字段的映射

```python
response = es.indices.get_field_mapping(fields="address", index="newbank")
```

### 3. 添加映射

```python
# 添加映射
body = {
  "properties": {
    "email":{
      "type": "keyword",
    }
  }
}
es.indices.put_mapping(body=body, index="new_index")
```

## 八、分词

```
# -*- coding: utf-8 -*-
# @Auther:Summer
from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch(["127.0.0.1:9200"])


# 使用普通的分词器进行分词
body = {
    "analyzer":"standard",
    "text":"我是中国人"
}

# 使用ik分词
body = {
    "analyzer":"ik_smart",
    "text":"我是中国人"
}
print(es.indices.analyze(body=body))
```



