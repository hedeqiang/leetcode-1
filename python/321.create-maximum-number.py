# [321] 拼接最大数

# https://leetcode-cn.com/problems/create-maximum-number/description/

# * algorithms
# * Hard (32.62%)
# * Total Accepted:    12.6K
# * Total Submissions: 31.2K
# * Testcase Example:  '[3,4,6,5]\n[9,1,2,5,8,3]\n5'

# 给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。

# 求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。

# 说明: 请尽可能地优化你算法的时间和空间复杂度。

# 示例 1:

# 输入:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# 输出:
# [9, 8, 6, 5, 3]

# 示例 2:

# 输入:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# 输出:
# [6, 7, 6, 0, 4]

# 示例 3:

# 输入:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# 输出:
# [9, 8, 9]


class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        def pick_max(nums, k):
            stack = []
            # 要取得k个就要丢掉剩余的
            drop = len(nums) - k
            # 构造单调递减栈
            for num in nums:
                # 还有要丢的名额
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            # 万一nums本身是单调的，可能一个都没drop掉，所以用k取一下保险
            return stack[:k]

        def merge(A, B):
            ans = []
            while A or B:
                # 注意元素、列表的直接比较
                bigger = A if A > B else B
                ans.append(bigger.pop(0))
            return ans

        return max(
            merge(pick_max(nums1, i), pick_max(nums2, k - i))
            for i in range(k + 1)
            if i <= len(nums1) and (k - i) <= len(nums2)
        )


# if __name__ == "__main__":
#     nums1 = [3, 4, 6, 5]
#     nums2 = [9, 1, 2, 5, 8, 3]
#     k = 5
#     res = Solution().maxNumber(nums1, nums2, 5)
#     print(res)
