# -*- coding: utf-8 -*-
from collections import deque


# 做法：
# 1. 先将所给的图根据字典创建起来，形成相应的嵌套
# 2. 创建一个队列，将第一个循环放入其中
# 3. 从队列中依次取值判断，如果这个值为所查的值，则返回该值。如果该值不是，则在队列末尾添加该值所对应的值。不管咋样都要在已经查找过列表中添加该值
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    return name == 'thom'

# search_queue = deque()
# search_queue += graph["you"]
# while search_queue:
#     person = search_queue.popleft()
#     if person_is_seller(person):
#         print(person + " is a mango seller!")
#         break
#     else:
#         search_queue += graph[person]


# 以上代码可能出现，当一个人已经被遍历之后，再次被另一个人遍历，若这个是一个无向的换，那么这个循环将进入一个无线的循环。因此得把代码修改成如下
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!" )
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search("you")
