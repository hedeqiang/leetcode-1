#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#
# https://leetcode-cn.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (43.14%)
# Total Accepted:    61.2K
# Total Submissions: 141.7K
# Testcase Example:  '"3+2*2"'
#
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
#
# 整数除法仅保留整数部分。
#
#
#
#
#
# 示例 1：
#
#
# 输入：s = "3+2*2"
# 输出：7
#
#
# 示例 2：
#
#
# 输入：s = " 3/2 "
# 输出：1
#
#
# 示例 3：
# 输入：s = " 3+5 / 2 "
# 输出：5
# 提示：
#
# 1
# s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
# s 表示一个 有效表达式
# 表达式中的所有整数都是非负整数，且在范围 [0, 2^31 - 1] 内
# 题目数据保证答案是一个 32-bit 整数


class Solution:
    def calculate(self, s: str) -> int:
        stack, num, sign = [], 0, "+"
        n = len(s)
        for i in range(n):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == n - 1:
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    tmp = stack.pop()
                    if tmp // num < 0 and tmp % num:
                        stack.append(tmp // num + 1)
                    else:
                        stack.append(tmp // num)
                sign = s[i]
                num = 0
        return sum(stack)
