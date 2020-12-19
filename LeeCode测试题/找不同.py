# -*- coding: utf-8 -*-
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # 1.ascii解法
        # num1,num2 = 0,0
        # for i in s:
        #     num1 += ord(i)
        # for i in t:
        #     num2 += ord(i)
        # num = num2 - num1
        # return chr(num)
        # 2.计数法
        s = Counter(s)
        t = Counter(t)
        for i in t:
            if t[i] != s[i]:
                return i


if __name__ == '__main__':
    s = "avd"
    t = "avdf"
    a = Solution()
    print(a.findTheDifference(s,t))