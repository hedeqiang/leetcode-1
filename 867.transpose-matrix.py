# [867] 转置矩阵

# https://leetcode-cn.com/problems/transpose-matrix/description/

# * algorithms
# * Easy (66.88%)
# * Total Accepted:    64.4K
# * Total Submissions: 94.3K
# * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'

# 给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。

# 矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。


#

# 示例 1：


# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[1,4,7],[2,5,8],[3,6,9]]


# 示例 2：


# 输入：matrix = [[1,2,3],[4,5,6]]
# 输出：[[1,4],[2,5],[3,6]]


#

# 提示：


# 	m == matrix.length
# 	n == matrix[i].length
# 	1
# 	1
# 	-10^9


class Solution(object):
    def transpose1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        return [
            [matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))
        ]

    def transpose0(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        ret = []
        for j in range(n):
            row = []
            for i in range(m):
                row.append(matrix[i][j])
            ret.append(row)
        return ret

    def transpose(self, matrix):
        return zip(*matrix)

