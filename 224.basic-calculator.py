# [224] 基本计算器

# https://leetcode-cn.com/problems/basic-calculator/description/

# * algorithms
# * Hard (41.90%)
# * Total Accepted:    52.4K
# * Total Submissions: 125K
# * Testcase Example:  '"1 + 1"'

# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

#

# 示例 1：


# 输入：s = "1 + 1"
# 输出：2


# 示例 2：


# 输入：s = " 2-1 + 2 "
# 输出：3


# 示例 3：


# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23


#

# 提示：


# 	1
# 	s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
# 	s 表示一个有效的表达式


class Solution:
    def calculate(self, s):
        ops = [1]
        sign = 1
        i, n = 0, len(s)
        res = 0

        while i < n:
            ch = s[i]
            if ch == " ":
                i += 1
            elif ch == "-":
                sign = -1 * ops[-1]
                i += 1
            elif ch == "+":
                sign = ops[-1]
                i += 1
            elif ch == "(":
                ops.append(sign)
                i += 1
            elif ch == ")":
                ops.pop()
                i += 1
            else:
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                res += sign * num
        return res

    def calculate0(self, s):
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == "+" or c == "-":
                res += sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res += sign * num
        return res


# res = Solution().calculate("3+2-5-6+1")
# print(res)
