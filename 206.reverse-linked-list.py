#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (58.66%)
# Total Accepted:    43.8K
# Total Submissions: 74K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList0(self, head: ListNode) -> ListNode:
        '''递归'''

        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head

    def reverseList(self, head: ListNode) -> ListNode:
        '''遍历'''
        pre, cur = None, head
        while cur:

            #tmp = cur.next
            #cur.next = pre
            #pre = cur
            #cur =  tmp

            # 不可以在修改了cur之后，再修改cur.next
            # 「= 」右边作为元组，值不会变
            #cur.next, pre, cur = pre, cur, cur.next
            cur.next, cur, pre = pre, cur.next, cur

        return pre

