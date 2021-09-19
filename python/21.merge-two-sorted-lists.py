#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (52.99%)
# Total Accepted:    55.9K
# Total Submissions: 104.4K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
#
#
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists0(self, l1, l2):
        head1, head2, dummy_head = l1, l2, ListNode(None)
        cur = dummy_head
        while head1 and head2:
            if head1.val <= head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        cur.next = head1 or head2
        return dummy_head.next

    def mergeTwoLists1(self, l1, l2):
        if l1 and l2:
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists1(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists1(l1, l2.next)
                return l2
        return l1 or l2

    def mergeTwoLists(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2


