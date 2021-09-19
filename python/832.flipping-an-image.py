# [832] 翻转图像

# https://leetcode-cn.com/problems/flipping-an-image/description/

# * algorithms
# * Easy (75.79%)
# * Total Accepted:    68.9K
# * Total Submissions: 86.8K
# * Testcase Example:  '[[1,1,0],[1,0,1],[0,0,0]]'

# 给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。

# 水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。

# 反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。


# 示例 1：


# 输入：[[1,1,0],[1,0,1],[0,0,0]]
# 输出：[[1,0,0],[0,1,0],[1,1,1]]
# 解释：首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
#      然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]


# 示例 2：


# 输入：[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# 输出：[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# 解释：首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
#      然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]


# 提示：


# 	1
# 	0


class Solution:
    def flipAndInvertImage0(self, A):
        for row in range(len(A)):
            A[row] = list(1 ^ i for i in A[row][::-1])
        return A

    def flipAndInvertImage(self, A):
        n = len(A)
        for row in range(n):
            left, right = 0, n-1
            # 左右指针
            # 1. 不同的时候交换了位置再取反，相当于不动
            # 2. 相同时候还剩取反操作
            while left < right:
                if A[row][left] == A[row][right]:
                    A[row][left] ^= 1
                    A[row][right] ^= 1
                left += 1
                right -= 1
            # 可能是奇数个数，剩中间位置没有被交换但是要取反
            if left == right:
                A[row][left] ^= 1
        return A


# A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
# res = Solution().flipAndInvertImage(A)
# print(res)
