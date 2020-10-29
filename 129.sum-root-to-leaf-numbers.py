# [129] 求根到叶子节点数字之和

# https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/description/

# * algorithms
# * Medium (66.16%)
# * Total Accepted:    61.1K
# * Total Submissions: 92K
# * Testcase Example:  '[1,2,3]'

# 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

# 例如，从根到叶子节点路径 1->2->3 代表数字 123。

# 计算从根到叶子节点生成的所有数字之和。

# 说明: 叶子节点是指没有子节点的节点。

# 示例 1:

# 输入: [1,2,3]
#     1
#    / \
#   2   3
# 输出: 25
# 解释:
# 从根到叶子节点路径 1->2 代表数字 12.
# 从根到叶子节点路径 1->3 代表数字 13.
# 因此，数字总和 = 12 + 13 = 25.

# 示例 2:

# 输入: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# 输出: 1026
# 解释:
# 从根到叶子节点路径 4->9->5 代表数字 495.
# 从根到叶子节点路径 4->9->1 代表数字 491.
# 从根到叶子节点路径 4->0 代表数字 40.
# 因此，数字总和 = 495 + 491 + 40 = 1026.


# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution(object):
    def sumNumbers0(self, root):
        res = [0]

        if not root:
            return 0

        def dfs(root, s):
            s = s * 10 + root.val
            if root.left:
                dfs(root.left, s)
            if root.right:
                dfs(root.right, s)
            if not (root.left or root.right):
                res[0] += s

        dfs(root, 0)
        return res[0]

    def sumNumbers(self, root):
        if not root:
            return 0
        res = 0
        node_queue = deque([root])
        num_queue = deque([root.val])

        while node_queue:
            node = node_queue.popleft()
            num = num_queue.popleft()
            if not (node.left or node.right):
                res += num
            else:
                if node.left:
                    node_queue.append(node.left)
                    num_queue.append(num * 10 + node.left.val)
                if node.right:
                    node_queue.append(node.right)
                    num_queue.append(num * 10 + node.right.val)
        return res
