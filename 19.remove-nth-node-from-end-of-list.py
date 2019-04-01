#
# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (32.51%)
# Total Accepted:    36.4K
# Total Submissions: 110.8K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
#
#
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？
#
#
# Definition for singly-linked list.


#  class ListNode(object):
    #  def __init__(self, x):
        #  self.val = x
        #  self.next = None


class Solution1(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy_head = ListNode(None)
        dummy_head.next = head
        cur, length = head, 0
        while cur:
            length += 1
            cur = cur.next

        length -= n
        cur = dummy_head
        while length > 0:
            length -= 1
            cur = cur.next
        cur.next = cur.next.next
        return dummy_head.next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 前后指针：前指针先走N步
        left, right = head, head
        for i in range(n):
            right = right.next
        # 如果走n步到头了，说明总共就N个节点
        if not right:
            return head.next

        # 将右指针走到头，总共需要length-N步
        # 左指针也同时走了length-N步，位于倒数第N的位置
        while right.next:
            right = right.next
            left = left.next
        # 移除节点，连接前后指节点
        left.next = left.next.next
        return head
