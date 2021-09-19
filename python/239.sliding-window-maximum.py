# [239] 滑动窗口最大值

# https://leetcode-cn.com/problems/sliding-window-maximum/description/

# * algorithms
# * Hard (49.21%)
# * Total Accepted:    82.6K
# * Total Submissions: 167.9K
# * Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'

# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

# 返回滑动窗口中的最大值。

#

# 进阶：

# 你能在线性时间复杂度内解决此题吗？

#

# 示例:

# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:

#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

#

# 提示：


# 	1 <= nums.length <= 10^5
# 	-10^4 <= nums[i] <= 10^4
# 	1 <= k <= nums.length

from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # window_loc为双端队列，左侧只记录每阶段窗口中最大值的索引
        # res保存各个窗口中的最大值
        window_loc, res = deque(), []
        for i, x in enumerate(nums):
            # 之前的滑动窗口长度满了，给这轮腾位置
            if window_loc and window_loc[0] + k <= i:
                window_loc.popleft()

            # 把之前比自己小的都干掉
            while window_loc and nums[window_loc[-1]] < x:
                window_loc.pop()
            # 每个值都会进入到位置窗口，都是潜在的现阶段最大值
            window_loc.append(i)

            # 填满一个滑动窗口，就记录其最大值
            if i >= k - 1:
                res.append(nums[window_loc[0]])
        return res
