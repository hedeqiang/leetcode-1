#
# @lc app=leetcode.cn id=86 lang=python
#
# [86] 分隔链表
#
# https://leetcode-cn.com/problems/partition-list/description/
#
# algorithms
# Medium (45.66%)
# Total Accepted:    7.7K
# Total Submissions: 16K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。
#
# 示例:
#
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
#
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head

        # 将大于等于的保存在新的链表
        rc = dummy_g = ListNode(None)

        pre = dummy = ListNode(None)
        cur = dummy.next = head

        while cur:
            # 大的移到新链表
            if cur.val >= x:
                pre.next, rc.next, rc, cur = cur.next, cur, cur, cur.next
            else:
                pre, cur = cur, cur.next

        # 清掉可能存在的小尾巴
        rc.next = None
        # 大链表接到原链表之后
        pre.next = dummy_g.next

        return dummy.next
