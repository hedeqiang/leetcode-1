#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#
# https://leetcode-cn.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (46.38%)
# Total Accepted:    57.4K
# Total Submissions: 110.7K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
#
#
#
#
#
# 示例 1：
#
#
# 输入：[3,2,3]
# 输出：[3]
#
# 示例 2：
#
#
# 输入：nums = [1]
# 输出：[1]
#
#
# 示例 3：
#
#
# 输入：[1,1,1,3,3,2,2,2]
# 输出：[1,2]
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
#
#
#
#
# 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。

# from collections import Counter
# from typing import List


class Solution:
    # def majorityElement0(self, nums: List[int]) -> List[int]:
    #     counter = Counter(nums)
    #     return [k for k, v in counter.items() if v > len(nums) / 3]

    def majorityElement(self, nums: List[int]) -> List[int]:
        v1, c1 = None, 0
        v2, c2 = None, 0

        # 三三消除
        for num in nums:
            if c1 and num == v1:
                c1 += 1
            elif c2 and num == v2:
                c2 += 1
            elif c1 == 0:
                c1 += 1
                v1 = num
            elif c2 == 0:
                c2 += 1
                v2 = num
            else:
                c1 -= 1
                c2 -= 1

        # 统计剩余的两个数
        cnt1, cnt2 = 0, 0
        for num in nums:
            if c1 > 0 and num == v1:
                cnt1 += 1
            elif c2 > 0 and num == v2:
                cnt2 += 1

        ret, one_thrid = [], len(nums) / 3
        if c1 > 0 and cnt1 > one_thrid:
            ret.append(v1)
        if c2 > 0 and cnt2 > one_thrid:
            ret.append(v2)
        return ret
