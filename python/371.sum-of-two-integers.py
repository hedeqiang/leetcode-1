#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#
# https://leetcode-cn.com/problems/sum-of-two-integers/description/
#
# algorithms
# Medium (58.04%)
# Total Accepted:    55.4K
# Total Submissions: 95.1K
# Testcase Example:  '1\n2'
#
# 给你两个整数 a 和 b ，不使用 运算符 + 和 - ​​​​​​​，计算并返回两整数之和。
#
#
#
# 示例 1：
#
#
# 输入：a = 1, b = 2
# 输出：3
#
#
# 示例 2：
#
#
# 输入：a = 2, b = 3
# 输出：5
#
#
#
#
# 提示：
#
#
# -1000 <= a, b <= 1000


MASK1 = 4294967296  # 2^32 32为整数溢出位
MASK2 = 2147483648  # 2^31 32位有符号整数符号位
MASK3 = 2147483647  # 2^31-1 最大的正整数

# 负数的表示：
# 除符号位之外，原码取反+1
# 比如-127 = 0b1000_0001
# 还原：0b0111_1111


class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            carry = ((a & b) << 1) % MASK1
            a = (a ^ b) % MASK1  # 只计算32位整形
            b = carry
        if a & MASK2:
            # 负数表示：除符号位之外，取反+1
            a = ~((a ^ MASK2) ^ MASK3)
            #      去掉符号位   取反
        return a
