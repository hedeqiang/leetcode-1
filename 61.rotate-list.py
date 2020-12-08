#
# @lc app=leetcode.cn id=61 lang=python
#
# [61] 旋转链表
#
# https://leetcode-cn.com/problems/rotate-list/description/
#
# algorithms
# Medium (37.51%)
# Total Accepted:    12.4K
# Total Submissions: 33K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
#
#
# 示例 2:
#
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
#
#
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or not head:
            return head

        dummy = ListNode(None)
        l = r = dummy.next = head

        # 先找到前后指针
        count = 0
        while count < k and r:
            r = r.next
            count += 1

        # 要求的长度比链表要长
        if not r:
            k = k % count
            return self.rotateRight(head, k)

        # r走到最后一个node，l就位于count-k的位置
        while r and r.next:
            r = r.next
            l = l.next

        dummy.next = l.next
        l.next = None
        r.next = head

        return dummy.next


class Solution0(object):
    """k的方向错了"""

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        l = dummy = ListNode(None)
        r = dummy.next = head

        count = 0
        while count < k and r:
            l = r
            r = r.next
            count += 1

        if not r:
            if count == k:
                return head
            k = k % count
            return self.rotateRight(head, k)

        l.next = None
        dummy.next = r

        while r.next:
            r = r.next

        r.next = head

        return dummy.next
