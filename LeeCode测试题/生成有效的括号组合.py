# -*- coding: utf-8 -*-
List = []


def generateParenthesis(n):
    _gen(0, 0, n, "")
    print(List)


def _gen(left, right, n, result):
    if left == n and right == n:
        List.append(result)
        return
    if left < n:
        _gen(left + 1, right, n, result + "(")
    if left > right and right < n:
        _gen(left, right + 1, n, result + ")")


if __name__ == '__main__':
    generateParenthesis(3)
