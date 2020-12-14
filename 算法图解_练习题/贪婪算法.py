# -*- coding: utf-8 -*-
# 贪婪算法：每一步都采用最优的做法
# 贪心算法（又称贪婪算法）是指，在对问题求解时，总是做出在当前看来是最好的选择。也就是说，不从整体最优上加以考虑，他所做出的是在某种意义上的局部最优解。
# 贪心算法不是对所有问题都能得到整体最优解，关键是贪心策略的选择，选择的贪心策略必须具备无后效性，即某个状态以前的过程不会影响以后的状态，只与当前状态有关。


states_needs = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}  # 要覆盖的州
stations = {}  # 存储每个电视台覆盖的州
stations["k1"] = {"id", "nv", "ut"}
stations["k2"] = {"wa", "id", "mt"}
stations["k3"] = {"or", "nv", "ca"}
stations["k4"] = {"nv", "ut"}
stations["k5"] = {"ca", "az"}
final_stations = set()  # 最终的电视台集合

while states_needs:  # 查看是否有未被覆盖的州
    best_station = None  # 用来存储覆盖最多的未覆盖州的广播电台
    states_covered = set()  # 包含该电台覆盖的所有未覆盖州
    for station, states_for_station in stations.items():
        covered = states_needs & states_for_station  # 包含同时出现在未覆盖州和该电台能覆盖的州的州
        if len(covered) > len(states_covered):  # 如果该州含有的为覆盖州大于现在已知的最大为覆盖州大小
            best_station = station
            states_covered = covered
    states_needs -= states_covered
    final_stations.add(best_station)

print(final_stations)
