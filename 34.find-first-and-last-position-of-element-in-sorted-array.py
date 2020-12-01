# [34] 在排序数组中查找元素的第一个和最后一个位置

# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

# * algorithms
# * Medium (41.58%)
# * Total Accepted:    173.3K
# * Total Submissions: 416.9K
# * Testcase Example:  '[5,7,7,8,8,10]\n8'

# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

# 如果数组中不存在目标值 target，返回 [-1, -1]。

# 进阶：


# 	你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？


#

# 示例 1：


# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]

# 示例 2：


# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]

# 示例 3：


# 输入：nums = [], target = 0
# 输出：[-1,-1]

#

# 提示：


# 	0
# 	-10^9
# 	nums 是一个非递减数组
# 	-10^9


class Solution(object):
    def searchRange_On(self, nums, target):
        first = -1
        last = -1
        for i, v in enumerate(nums):
            if v == target:
                if first == -1:
                    first = i
                last = i

        return [first, last]

    def searchRange(self, nums, target):
        left_index = nums.index(target)
        if left_index == len(nums) - 1 or nums[left_index] != target:
            return [-1, -1]



# if __name__ == "__main__":
#     res = Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=6)
#     print(res)
#     res = Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=8)
#     print(res)
