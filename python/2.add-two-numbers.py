#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (33.13%)
# Total Accepted:    104.7K
# Total Submissions: 312K
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s = self.walk_to_add(l1) + self.walk_to_add(l2)

        s, r = divmod(s, 10)
        cur = head = ListNode(r)
        while s > 0:
            s, r = divmod(s, 10)
            cur.next = ListNode(r)
            cur = cur.next

        return head

    def walk_to_add(self, l: ListNode) -> int:
        n, i, cur = 0, 0, l
        while cur:
            n += 10**i * cur.val
            i += 1
            cur = cur.next
        return n


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = l1, l2
        cur = dummy_head = ListNode(0)
        carry = 0
        while p or q or carry:
            x = p.val if p else 0
            y = q.val if q else 0
            carry += x + y
            carry, r = divmod(carry, 10)

            cur.next = ListNode(r)
            cur = cur.next

            if q:
                q = q.next
            if p:
                p = p.next

        return dummy_head.next




