# -*- coding: utf-8 -*-


def countConsistentStrings(allowed, words):
    ans = 0
    allowed = set(list(allowed))
    for i in words:
        i = set(list(i))
        if i | allowed == allowed:
            ans += 1
    return ans


if __name__ == '__main__':
    print(countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"]))
