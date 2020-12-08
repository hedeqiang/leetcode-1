# [861] Score After Flipping Matrix

# https://leetcode-cn.com/problems/score-after-flipping-matrix/description/

# * algorithms
# * Medium (74.51%)
# * Total Accepted:    27.2K
# * Total Submissions: 33.5K
# * Testcase Example:  '[[0,0,1,1],[1,0,1,0],[1,1,0,0]]'

# 有一个二维矩阵 A 其中每个元素的值为 0 或 1 。

# 移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。

# 在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。

# 返回尽可能高的分数。

#


# 示例：

# 输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# 输出：39
# 解释：
# 转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

#

# 提示：


# 	1 <= A.length <= 20
# 	1 <= A[0].length <= 20
# 	A[i][j] 是 0 或 1


class Solution:
    def matrixScore(self, A):
        m, n, ans = len(A), len(A[0]), 0
        for c in range(n):
            # 与行首值相同的列数：行首是0，那么跟着变1；行首是1，保持不变
            col = sum(A[r][c] == A[r][0] for r in range(m))
            # 每个列都要最终invert出最多的1，这个值要么是col，要么是`行数-col`
            ans += max(col, m - col) * 2 ** (n - 1 - c)
        return ans
