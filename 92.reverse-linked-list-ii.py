#
# @lc app=leetcode.cn id=92 lang=python
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (42.06%)
# Total Accepted:    9.7K
# Total Submissions: 22.5K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if n == 1 or m == n or not head:
            return head

        pre = dummy = ListNode(None)
        cur = dummy.next = head

        # 找到区间之外左边点l
        for _ in range(m - 1):
            pre, cur = cur, cur.next
        l = pre
        # 保存新的交换区间尾部位置

        # 找到区间之外右边点r
        for _ in range(n - m):
            cur = cur.next
        r = cur.next

        # 区间内反转
        pre, cur = l, pre.next
        while cur is not r:
            cur.next, cur, pre = pre, cur.next, cur

        # 重新连接区间两边指针
        l.next.next = r
        l.next = pre

        return dummy.next
