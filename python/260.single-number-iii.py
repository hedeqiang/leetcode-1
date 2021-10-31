#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#
# https://leetcode-cn.com/problems/single-number-iii/description/
#
# algorithms
# Medium (74.14%)
# Total Accepted:    75.7K
# Total Submissions: 102K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
#
# 进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
#
# 示例 1：
#
# 输入：nums = [1,2,1,3,2,5]
# 输出：[3,5]
# 解释：[5, 3] 也是有效的答案。
#
# 示例 2：
#
# 输入：nums = [-1,0]
# 输出：[-1,0]
#
# 示例 3：
#
# 输入：nums = [0,1]
# 输出：[1,0]
#
# 提示：
#
# 2
# -2^31
# 除两个只出现一次的整数外，nums 中的其他数字都出现两次

from typing import List
from functools import reduce
from operator import xor


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorsum = reduce(xor, nums)
        type1 = type2 = 0
        lsb = xorsum & -xorsum
        for num in nums:
            if num & lsb:
                type1 ^= num
            else:
                type2 ^= num
        return [type1, type2]
