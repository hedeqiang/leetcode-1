# [164] 最大间距

# https://leetcode-cn.com/problems/maximum-gap/description/

# * algorithms
# * Hard (55.16%)
# * Total Accepted:    39.1K
# * Total Submissions: 64.5K
# * Testcase Example:  '[3,6,9,1]'

# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

# 如果数组元素个数小于 2，则返回 0。

# 示例 1:

# 输入: [3,6,9,1]
# 输出: 3
# 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。

# 示例 2:

# 输入: [10]
# 输出: 0
# 解释: 数组元素个数小于 2，因此返回 0。

# 说明:


# 	你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
# 	请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。


class Solution(object):
    def maximumGap(self, nums):
        length = len(nums)
        if length < 2:
            return 0

        max_ = max(nums)
        min_ = min(nums)
        range_ = max_ - min_
        max_gap = 0

        each_bucket_size = max(1, range_ // (length - 1))
        bucket_num = (range_ // each_bucket_size) + 1

        buckets = [[] for _ in range(bucket_num)]

        for x in nums:
            loc = (x - min_) // each_bucket_size
            buckets[loc].append(x)

        prev_max = float("inf")
        for bucket in buckets:
            if bucket and prev_max != float("inf"):
                max_gap = max(max_gap, min(bucket) - prev_max)

            if bucket:
                prev_max = max(bucket)

        return max_gap
