# [941] 按奇偶排序数组

# https://leetcode-cn.com/problems/valid-mountain-array/description/

# * algorithms
# * Easy (36.19%)
# * Total Accepted:    22.4K
# * Total Submissions: 58.6K
# * Testcase Example:  '[2,1]'

# 给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。

# 让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

# 	A.length >= 3
# 	在 0 < i < A.length - 1 条件下，存在 i 使得：

# 		A[0] < A[1] < ... A[i-1] < A[i]
# 		A[i] > A[i+1] > ... > A[A.length - 1]

# 示例 1：

# 输入：[2,1]
# 输出：false

# 示例 2：

# 输入：[3,5,5]
# 输出：false

# 示例 3：

# 输入：[0,3,2,1]
# 输出：true

# 提示：

# 	0 <= A.length <= 10000
# 	0 <= A[i] <= 10000


class Solution(object):
    def validMountainArray(self, A):
        n = len(A)
        if n < 3:
            return False

        i = 1
        while i < n and A[i] > A[i - 1]:
            i += 1

        # 没上过坡/没遇到过下坡/遇到平路
        if i == 1 or i >= n or A[i] == A[i - 1]:
            return False

        while i < n and A[i] < A[i - 1]:
            i += 1

        # 下坡到底就ok
        return i >= n
