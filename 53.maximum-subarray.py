# [53] 最大子序和

# https://leetcode-cn.com/problems/maximum-subarray/description/

# * algorithms
# * Easy (52.58%)
# * Total Accepted:    349.6K
# * Total Submissions: 664.9K
# * Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'

# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 示例:

# 输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


# 进阶:

# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # s = nums[0]
        # max_list = [s]
        for i in range(1, len(nums)):
            # 还在变大就累加，否则新来的就已经是最大
            # s = max(nums[i], nums[i] + s)
            # 保存每个阶段最大值
            # max_list.append(s)
            nums[i] = max(nums[i-1] + nums[i], nums[i])
        return max(nums)
