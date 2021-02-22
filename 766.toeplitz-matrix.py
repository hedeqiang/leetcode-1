# [766] 扁平化多级双向链表

# https://leetcode-cn.com/problems/toeplitz-matrix/description/

# * algorithms
# * Easy (67.12%)
# * Total Accepted:    40.4K
# * Total Submissions: 57.2K
# * Testcase Example:  '[[1,2,3,4],[5,1,2,3],[9,5,1,2]]'

# 给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。

# 如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。

#

# 示例 1：


# 输入：matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# 输出：true
# 解释：
# 在上述矩阵中, 其对角线为:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。
# 各条对角线上的所有元素均相同, 因此答案是 True 。


# 示例 2：


# 输入：matrix = [[1,2],[2,2]]
# 输出：false
# 解释：
# 对角线 "[1, 2]" 上的元素不同。

#

# 提示：

# 	m == matrix.length
# 	n == matrix[i].length
# 	1
# 	0

#

# 进阶：

# 	如果矩阵存储在磁盘上，并且内存有限，以至于一次最多只能将矩阵的一行加载到内存中，该怎么办？
# 	如果矩阵太大，以至于一次只能将不完整的一行加载到内存中，该怎么办？

from collections import deque

class Solution(object):
    def isToeplitzMatrix0(self, matrix):
        # 左上角有数字的位置才需要关心
        # 最左上角的位置会是0，0，所以从1，1开始
        m = len(matrix)
        n = len(matrix[0])
        for x in range(1, m):
            for y in range(1, n):
                if matrix[x][y] != matrix[x - 1][y - 1]:
                    return False
        return True

    def isToeplitzMatrix1(self, matrix):
        if not matrix or len(matrix) <= 1:
            return True
        m = len(matrix)
        n = len(matrix[0])

        # upper
        for col in range(0, n):
            val = matrix[0][col]
            i, j = 0, col
            while i < m and j < n:
                if matrix[i][j] != val:
                    return False
                i += 1
                j += 1

        # lower
        for row in range(1, m):
            val = matrix[row][0]
            i, j = row, 0
            while i < m and j < n:
                if matrix[i][j] != val:
                    return False
                i += 1
                j += 1

        return True


    def isToeplitzMatrix(self, matrix):
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])

        expected = deque(matrix[0])
        for row_idx in range(1, m):
            row = matrix[row_idx]
            # 将期望行右移1位：丢掉最右边，用读取行最左位补齐，下一轮用
            expected.pop()
            expected.appendleft(row[0])

            # 从偏移位置开始比较
            for i in range(1, n):
                if not expected[i] == row[i]:
                    return False
        return True

        """
        1, 2, 3, 4   ->          1, 2, 3, 4    : pop 4
        5, 1, 2, 3   ->       5, 1, 2, 3       : pop 3
        6, 5, 1, 2   ->    6, 5, 1, 2          : pop 2
        7, 6, 5, 1   -> 7, 6, 5, 1
        """
