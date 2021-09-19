#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
# https://leetcode-cn.com/problems/word-search-ii/description/
#
# algorithms
# Hard (44.96%)
# Total Accepted:    51.7K
# Total Submissions: 113.3K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' + '["oath","pea","eat","rain"]'
#
# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。
#
# 单词必须按照字母顺序，通过 相邻的单元格
# 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
#
#
#
# 示例 1：
#
#
# 输入：board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# 输出：["eat","oath"]
#
#
# 示例 2：
#
#
# 输入：board = [["a","b"],["c","d"]], words = ["abcb"]
# 输出：[]
#
#
#
#
# 提示：
#
#
# m == board.length
# n == board[i].length
# 1
# board[i][j] 是一个小写英文字母
# 1
# 1
# words[i] 由小写英文字母组成
# words 中的所有字符串互不相同

from typing import List
from collections import defaultdict


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class Trie:
            def __init__(self):
                self.children = defaultdict(Trie)
                self.word = ""

            def add_word(self, word):
                cur = self
                for c in word:
                    cur = cur.children[c]
                cur.word = word

        trie = Trie()
        for word in words:
            trie.add_word(word)

        def dfs(now, i1, j1):
            # 当前字符不属于任何一个单词，结束
            if board[i1][j1] not in now.children:

                return

            ch = board[i1][j1]
            # 加上当前字符之后的字典树
            nxt = now.children[ch]

            # 当前单词匹配
            if nxt.word != "":
                ans.append(nxt.word)
                # 避免之后重复添加
                nxt.word = ""

            #  新字典树下，还有单词，继续查找上下左右，不走走过的路径
            if nxt.children:
                board[i1][j1] = "#"
                for i2, j2 in [(i1 + 1, j1), (i1 - 1, j1), (i1, j1 + 1), (i1, j1 - 1)]:
                    if 0 <= i2 < m and 0 <= j2 < n:
                        dfs(nxt, i2, j2)
                board[i1][j1] = ch

            if not nxt.children:
                # 走到这里有两种情况：
                # 1、这是叶子结点，则必为word，已经被匹配上，添加了
                # 2、这不是叶子结点，下面的结点都被删光了
                #   （下面叶子单词都匹配上了，这个路径不需要再看了）
                now.children.pop(ch)

        ans = []
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)

        return ans


# board = [
#     ["o", "a", "a", "n"],
#     ["e", "t", "a", "e"],
#     ["i", "h", "k", "r"],
#     ["i", "f", "l", "v"],
# ]
# words = ["oath", "pea", "eat", "rain"]

# ans = Solution().findWords(board=board, words=words)
# print(ans)
