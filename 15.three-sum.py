# [15] 三数之和

# https://leetcode-cn.com/problems/3sum/description/

# * algorithms
# * Medium (29.85%)
# * Total Accepted:    351.6K
# * Total Submissions: 1.2M
# * Testcase Example:  '[-1,0,1,2,-1,-4]'

# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

#

# 示例：

# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution(object):
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, a in enumerate(nums[:-2]):
            if i >= 1 and nums[i - 1] == a:
                continue
            d = {}
            # 转换为two-sum，且b就是最后剩下要找的那个值
            for b in nums[i + 1 :]:
                if b in d:
                    res.add((a, -a - b, b))
                else:
                    d[-a - b] = 1
        return [list(l) for l in res]
