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
        # 有序，用二分查找
        def _binary_search(nums, target, lower):
            left, right = 0, len(nums) - 1
            # ans初始化为一个可以判定不合理的值
            # 最后left, right跳出，判断对应位置是否等于target 👍
            ans = len(nums)
            while left <= right:
                mid = (left + right) // 2
                # 不够小，或者相等情况下要找更小的位置，就往左边挤压
                if nums[mid] > target or (lower and nums[mid] >= target):
                    right = mid - 1
                    ans = mid
                # 太大了，需要往右边看。找到相等的，需要往右边看看还有没有相等的
                else:
                    left = mid + 1
            return ans

        left_index = _binary_search(nums, target, True)
        right_index = _binary_search(nums, target, False) - 1
        if (
            left_index <= right_index
            and right_index < len(nums)
            and nums[left_index] == target
            and nums[right_index] == target
        ):
            return [left_index, right_index]
        return [-1, -1]


# if __name__ == "__main__":
#     res = Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=6)
#     print(res)
#     res = Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=8)
#     print(res)
