# -*- coding: utf-8 -*-


# 如果存在环，则需要忽略环
infnum = float("inf")
# 创建graph表
graph = {"A": {"B": 10}, "B": {"D": 20}, "C": {"B": 1}, "D": {"C": 1}, "E": {}}

# 创建costs表
costs = {"B": 10, "C": infnum, "D": infnum, "E": infnum}

# 创建parents表
parents = {"B": "A", "D": None, "C": None, "E": None}

# 创建selected来存储已经查找过的点
selected = []


# 创建查找最低开销点
def find_lowest_cost_node(costs):
    print(costs)
    lowest_cost = infnum
    lowest_cost_node = None
    for node in costs:  # 循环读取costs中所有的点，查找最低开销点
        now_cost = costs[node]  # 获取当前点的开销
        if lowest_cost > now_cost and node not in selected:  # 如果当前节点的开销更低且未处理过，
            lowest_cost = now_cost  # 就将其视为开销最低的节点
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:  # 在未处理的节点中找出开销最小的节点
    print(node)
    cost = costs[node]  # 获取该结点的当前开销
    neighbours = graph[node]  # 获取该结点的所有邻居结点
    for n in neighbours:  # 遍历当前节点的所有邻居
        now_cost = cost + neighbours[n]
        if costs[n] > now_cost:  # 如果经当前节点前往该邻居更近，
            costs[n] = now_cost  # 就更新该邻居的开销
            parents[n] = node  # 同时将该邻居的父节点设置为当前节点
    selected.append(node)
    node = find_lowest_cost_node(costs)  # 找出接下来要处理的节点，并循环
