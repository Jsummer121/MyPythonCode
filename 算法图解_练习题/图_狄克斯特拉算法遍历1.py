# -*- coding: utf-8 -*-


# 做法:
# 1. 先根据题目创建出三个表:第一个表示根据图所创建的迭代的字典,第二个是创建的每个节点所对应的开销或权重,第三个是保存该节点的最低开销结点的父节点
# 2. 创建查找函数,遍历开销表的每一个节点,查找出当前开销表中最低开销值的结点,并且该结点必须是不能被使用过的,返回该节点
# 3. 根据查找函数所返回的值,获取该结点的当前最低开销和该节点的邻居结点。根据该节点的邻居结点循环判断当前节点到邻居结点的开销是否比该邻居结点保存在开销表中的值小，如果小，则将该邻居结点在表中的值转化为当前开销，并且将父表中的邻居结点的父节点改为当前节点
infnum = float("inf")  # 最大数
# graph表的创建
graph = {}
graph["A"] = {}
graph["A"]["B"] = 5
graph["A"]["C"] = 2
graph["B"] = {}
graph["B"]["D"] = 4
graph["B"]["E"] = 2
graph["C"] = {}
graph["C"]["B"] = 8
graph["C"]["E"] = 7
graph["D"] = {}
graph["D"]["E"] = 6
graph["D"]["F"] = 3
graph["E"] = {}
graph["E"]["F"] = 1
graph["F"] = {}

# costs表创建
costs = {"B": 5, "C": 2, "D": infnum, "E": infnum, "F": infnum}

# parents表创建
parents = {"B": "A", "C": "A", "D": None, "E": None, "F": None}

# 创建已经遍历过的表
selected = []


# 创建查找开销最小的点
def find_lowest_cost_node(costs):
    lowest_cost = infnum
    lowest_cost_node = None
    for node in costs:  # 遍历costs中所有的结点
        cost = costs[node]  # 获取当前节点的最低开销
        if cost < lowest_cost and node not in selected:  # 如果当前节点的开销更低并且未被处理
            lowest_cost = cost  # 将其视为最低开销结点
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]  # 从开销表中获取当前节点的最低开销
    neighbours = graph[node]  # 获取该结点的邻居结点
    for n in neighbours:  # 遍历邻居结点
        new_cost = cost + neighbours[n]  # 根据现有的结点加上邻居结点的距离
        if costs[n] > new_cost:  # 如果最低开销比现在的还大，则换值
            costs[n] = new_cost
            parents[n] = node
    selected.append(node)
    node = find_lowest_cost_node(costs)

node = parents["F"]
while node != "A":
    print("该结点为：" + node)
    node = parents[node]
