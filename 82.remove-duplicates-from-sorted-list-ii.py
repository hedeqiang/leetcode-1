#
# @lc app=leetcode.cn id=82 lang=python
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (39.57%)
# Total Accepted:    8.1K
# Total Submissions: 20.5K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
# 
# 示例 1:
# 
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 
# 
# 示例 2:
# 
# 输入: 1->1->1->2->3
# 输出: 2->3
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy_head = ListNode(None)
        dummy_head.next = head
        pre, slow, fast = dummy_head, head, head.next

        flag = False
        while fast:
            if fast.val == slow.val:
                flag = True
                fast = fast.next
            else:
                if flag:
                    pre.next = fast
                    flag = False
                else:
                    pre = slow
                slow = fast
                fast = fast.next
        if flag:
            pre.next = None

        return dummy_head.next

