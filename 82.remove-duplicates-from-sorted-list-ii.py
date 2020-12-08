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


class Solution0(object):
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

        # 通过flag来标记是否在处理相等的情况
        flag = False
        while fast:
            if fast.val == slow.val:
                flag = True
            else:
                if flag:
                    # 相等结束，将相等部分全部跳过
                    # 通过pre.next重新定位
                    pre.next = fast
                    flag = False
                else:
                    # 遇到不相等情况，前节点指针后移
                    pre = slow
                # 遇到不相等情况，慢指针指向快指针
                slow = fast
            # 无论哪种情况，快指针往后移
            fast = fast.next
        if flag:
            pre.next = None

        return dummy_head.next


class Solution:
    def deleteDuplicates(self, head):
        dummy_head = pre = ListNode(None)
        dummy_head.next = cur = head
        while cur and cur.next:
            # 遇到相等的，就把所有相等的都走完
            if cur.val == cur.next.val:
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
                pre.next = cur
            else:
                pre = pre.next
                cur = cur.next
        return dummy_head.next
