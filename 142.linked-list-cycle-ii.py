#
# @lc app=leetcode.cn id=142 lang=python
#
# [142] 环形链表 II
#
# https://leetcode-cn.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (35.11%)
# Total Accepted:    14.9K
# Total Submissions: 38.9K
# Testcase Example:  '[3,2,0,-4]\n1'
#
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
# 
# 说明：不允许修改给定的链表。
# 
# 
# 
# 示例 1：
# 
# 输入：head = [3,2,0,-4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
# 
# 
# 
# 
# 示例 2：
# 
# 输入：head = [1,2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
# 
# 
# 
# 
# 示例 3：
# 
# 输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。
# 
# 
# 
# 
# 
# 
# 进阶：
# 你是否可以不用额外空间解决此题？
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast is slow:
                # loop的长度为l
                # slow_steps = m + k; 其中m是起始点head到环起始点距离，k是环起始点到相遇点距离;

                # fast走的步长为slow两倍
                # fast_steps = slow_steps * 2 = slow_steps + N * l, 其中N=1,2,3,4,5.... 
                # 所以 slow_steps = N*l, 即m + k = N * l
                # p从头走m+k步，等于q绕N圈；p从头走m步，等于q绕N圈往回退k步，正好位于环起始点，pq会相遇
                slow = head
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None
