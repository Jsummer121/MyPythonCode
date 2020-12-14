# -*- coding: utf-8 -*-
def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    s = "11"
    a = ""
    if n == 1:
        return "1"
    if n == 2:
        return s
    j = 1
    for k in range(n - 2):
        for i in range(len(s) - 1):
            if i == len(s) - 2:
                if s[i] == s[i + 1]:
                    j += 1
                    a += str(j) + s[i]
                    j = 1
                else:
                    a += str(j) + s[i]
                    a += "1" + s[i + 1]
                    j = 1
            else:
                if s[i] == s[i + 1]:
                    j += 1
                else:
                    a += str(j) + s[i]
                    j = 1
        s = a
        a = ""
    return s

print(countAndSay(4))