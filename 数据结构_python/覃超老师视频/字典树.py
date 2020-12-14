# -*- coding: utf-8 -*-


# Trie树，即字典树，又称单词查找树或键树，是一种树形结构，是一种哈稀树的变种。
# 优点：最大限度地减少无畏的字符串比较，查询效率比哈希表高
# 思想：空间换时间
# 基本性质：（1）根节点不包含字符，除根节点外的每一个节点都只包含一个字符
# （2）从根节点到某个节点，路径上经过的字符串连接起来，为该结点对应的字符串。
# （3）每个节点的所有子节点包含的字符都不相同

class TrieNode(object):
    def __init__(self):
        # self.childern = [None] * ALPHABET_SIZE
        # self.isEndOfWord = False
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


