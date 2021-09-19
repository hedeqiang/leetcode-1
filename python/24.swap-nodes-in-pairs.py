#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (57.77%)
# Total Accepted:    16.7K
# Total Submissions: 28.6K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
# 示例:
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
#
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = dummy = ListNode(None)
        dummy.next = cur = head
        while cur and cur.next:
            #  cur.next.next, pre.next, cur.next, pre, cur = cur, cur.next, cur.next.next, cur, cur.next.next
            pre.next, pre = cur.next, cur
            cur.next.next, cur.next, cur = cur, cur.next.next, cur.next.next

        return dummy.next
