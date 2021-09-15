#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
#
# https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/description/
#
# algorithms
# Medium (47.25%)
# Total Accepted:    41.8K
# Total Submissions: 87.7K
# Testcase Example:  '"abpcplea"\n["ale","apple","monkey","plea"]'
#
# 给你一个字符串 s 和一个字符串数组 dictionary 作为字典，找出并返回字典中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
#
# 如果答案不止一个，返回长度最长且字典序最小的字符串。如果答案不存在，则返回空字符串。
#
#
#
# 示例 1：
#
#
# 输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
# 输出："apple"
#
#
# 示例 2：
#
#
# 输入：s = "abpcplea", dictionary = ["a","b","c"]
# 输出："a"
#
#
#
#
# 提示：
#
#
# 1
# 1
# 1
# s 和 dictionary[i] 仅由小写英文字母组成

# from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        for d in dictionary:
            i = j = 0
            while i < len(d) and j < len(s):
                if d[i] == s[j]:
                    i += 1
                j += 1
            if i == len(d):
                return d
        return ""
