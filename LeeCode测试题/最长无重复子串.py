# -*- coding: utf-8 -*-
def lengthOfLongestSubstring(s):
    # st = {}  # 记录以某个字符结束时，它的最长子序列长度
    # i, ans = 0, 0
    # for j in range(len(s)):
    #     if s[j] in st:  # 如果该值已经出现在前面过
    #         i = max(st[s[j]], i)  # 则判断它的最长子串长度与当前的i哪个大，
    #     ans = max(ans, j - i + 1)
    #     st[s[j]] = j + 1
    # print(ans)
    # 哈希集合，记录每个字符是否出现过
    occ = set()
    n = len(s)
    rk, ans = 0, 0
    for i in range(n):
        if i != 0:
            # 除了第一次进去的时候是内部没有元素的，后面的每一次进入都有可能出现与当前下标相同的字母，所以应该将该字母删除，然后重新计数，进入下一次循环
            occ.remove(s[i - 1])
        while rk < n and s[rk] not in occ:  # 如过右指针不超过边界并且右指针所指的元素没有保存在occ中
            # 则不断地移动右指针，并且将下标所指的值放入occ
            occ.add(s[rk])
            rk += 1
        # 第 i 到 rk 个字符是一个极长的无重复字符子串
        ans = max(ans, rk - i)
    print(ans)


if __name__ == '__main__':
    lengthOfLongestSubstring("aaaaaa")