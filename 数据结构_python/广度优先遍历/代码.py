# -*- coding: utf-8 -*-
from collections import deque  # 从collections库中导入deque类

graph = {}
graph["A"] = ["B", "C", "F"]
graph["B"] = []
graph["C"] = ["E", "F", "D"]
graph["D"] = ["H", "G"]
graph["E"] = ["I"]
graph["F"] = []
graph["G"] = []
graph["H"] = ["I"]
graph["I"] = []


def person_is_seller(person):  # 创建判断函数，查看该人是否是I
    return person == "I"


def search(name):
    search_people = deque()  # 创建一个队列
    search_people += graph[name]  # 将name的朋友加入到队列中
    searched = []
    while search_people:  # 如果队列不为空
        person = search_people.popleft()  # 取出当前队列的第一个人
        if not person in searched:  # 如果这个人没有被查找过
            if person_is_seller(person):  # 检查这个人是否是I
                print(person + " is a love tree'people!")  # 是I
                break
            else:
                search_people += graph[person]  # 如果不是，则把这个人的朋友都加入到队列张红
    return False

search("A")