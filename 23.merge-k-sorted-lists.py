#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (43.89%)
# Total Accepted:    18.1K
# Total Submissions: 40.9K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
#
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head1, head2, dummy_head = l1, l2, ListNode(None)
        cur = dummy_head
        while head1 or head2:
            if not head1:
                cur.next = head2
                break
            if not head2:
                cur.next = head1
                break
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        return dummy_head.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        # 所有依次排，超时
        # merged_list = lists[0]
        # for i in range(1, len(lists)):
        #    merged_list = self.mergeTwoLists(merged_list, lists[i])

        # 左右分割，分而治之
        mid = len(lists) / 2
        left_lists = lists[:mid]
        right_lists = lists[mid:]
        return self.mergeTwoLists(
            self.mergeKLists(left_lists), self.mergeKLists(right_lists)
        )
