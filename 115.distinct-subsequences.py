#!/usr/bin/env python3
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#
# https://leetcode-cn.com/problems/distinct-subsequences/description/
#
# algorithms
# Hard (50.14%)
# Total Accepted:    38.6K
# Total Submissions: 72.7K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# 给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
#
# 字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE"
# 的一个子序列，而 "AEC" 不是）
#
# 题目数据保证答案符合 32 位带符号整数范围。
#
#
#
# 示例 1：
#
#
# 输入：s = "rabbbit", t = "rabbit"
# 输出：3
# 解释：
# 如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
# (上箭头符号 ^ 表示选取的字母)
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
#
#
# 示例 2：
#
#
# 输入：s = "babgbag", t = "bag"
# 输出：5
# 解释：
# 如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。
# (上箭头符号 ^ 表示选取的字母)
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
# ⁠ ^  ^^
# babgbag
# ⁠   ^^^
#
#
#
# 提示：
#
#
# 0
# s 和 t 由英文字母组成
#
#
#


# def print_dp(dp):
#     for row in dp:
#         print(row)


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        slen, tlen = len(s), len(t)
        dp = [[None] * (slen + 1) for _ in range(tlen + 1)]
        # t为空的时候，是任何长度s的子串
        for j in range(slen + 1):
            dp[0][j] = 1
        # s为空的时候为，任何非0长度的t都不是它的子串
        for i in range(1, tlen + 1):
            dp[i][0] = 0

        # print_dp(dp)

        for i in range(1, tlen + 1):
            for j in range(1, slen + 1):
                # 如果相等，s使用当前字符或者不使用当前字符
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                # 如果不相等，s用不上当前字符
                else:
                    dp[i][j] = dp[i][j - 1]
        # print_dp(dp)
        return dp[-1][-1]


# s = "rabbbit"
# t = "rabbit"
# res = Solution().numDistinct(s, t)
# print(res)
