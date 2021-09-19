# [144] 二叉树的前序遍历

# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/

# * algorithms
# * Medium (68.36%)
# * Total Accepted:    219.3K
# * Total Submissions: 320.8K
# * Testcase Example:  '[1,null,2,3]'

# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

# 示例 1：

# 输入：root = [1,null,2,3]
# 输出：[1,2,3]

# 示例 2：

# 输入：root = []
# 输出：[]

# 示例 3：

# 输入：root = [1]
# 输出：[1]

# 示例 4：

# 输入：root = [1,2]
# 输出：[1,2]

# 示例 5：

# 输入：root = [1,null,2]
# 输出：[1,2]

# 提示：

# 	树中节点数目在范围 [0, 100] 内
# 	-100

# 进阶：递归算法很简单，你可以通过迭代算法完成吗？

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def preorderTraversal(self, root):
        stack = []
        res = []
        node = root
        while stack or node:
            # 一定会走到最左边
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            # 到这里说明已经进入过叶子节点的左边
            # 可以从栈里处理新值，且栈里取出来的值，不用再考虑左子树
            if stack:
                node = stack.pop()
                node = node.right
        return res
