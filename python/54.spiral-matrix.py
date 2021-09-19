# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode-cn.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (43.22%)
# Total Accepted:    129.4K
# Total Submissions: 284.1K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
#

#
# 示例 1：
#
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
#
# 示例 2：
#
#
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1
# -100
#
#
#
from typing import List


class Solution:
    def spiralOrder0(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        rows_size, cols_size = len(matrix), len(matrix[0])
        total = rows_size * cols_size
        count = 0
        row, col = 0, 0
        # right, down, left, up
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        index = 0
        visited_matrix = [[False] * cols_size for _ in range(rows_size)]
        ret = []
        while count < total:
            # print(f"{ row= }, { col= }, { index= }")
            ret.append(matrix[row][col])
            count += 1
            visited_matrix[row][col] = True

            next_row, next_col = row + directions[index][0], col + directions[index][1]
            if (
                0 <= next_row < rows_size
                and 0 <= next_col < cols_size
                and not visited_matrix[next_row][next_col]
            ):
                row, col = next_row, next_col
            else:
                index = (index + 1) % 4
                row, col = row + directions[index][0], col + directions[index][1]
        return ret

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        ret = []
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        i, j = 0, 0
        while l <= r and t <= b:
            # right
            for j in range(l, r + 1):
                ret.append(matrix[t][j])
            # down
            for i in range(t + 1, b + 1):
                ret.append(matrix[i][r])
            if l < r and t < b:
                # left
                for j in range(r - 1, l, -1):
                    ret.append(matrix[b][j])
                # up
                for i in range(b, t, -1):
                    ret.append(matrix[i][l])

            l, r, t, b = l + 1, r - 1, t + 1, b - 1

        return ret


# m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ret = Solution().spiralOrder(m)
# print(ret)
# ret = Solution().spiralOrder0(m)
# print(ret)
