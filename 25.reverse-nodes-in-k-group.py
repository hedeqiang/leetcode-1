# coding: utf-8
# @lc app=leetcode.cn id=25 lang=python
#
# [25] k个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (49.68%)
# Total Accepted:    8.8K
# Total Submissions: 17.5K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。
#
# 示例 :
#
# 给定这个链表：1->2->3->4->5
#
# 当 k = 2 时，应当返回: 2->1->4->3->5
#
# 当 k = 3 时，应当返回: 3->2->1->4->5
#
# 说明 :
#
#
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
# Definition for singly-linked list.


class Solution0(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:  # 使用r来定位区间
                r = r.next
                count += 1
            if count == k:  # 有k个了就把r,l之间反转
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # pre作为头，从l开始从后往前指
                jump.next, jump, l = (
                    pre,
                    l,
                    r,
                )  # 反转结束后，pre位于原来的尾，现在要作为头连接到之前的节点jump，原来的头(l)位于尾巴，要成为新的jump
            else:
                return dummy.next


class Solution:
    def reverseKGroup(self, head, k):
        if k < 2:
            return head

        node = head
        for _ in range(k):
            if not node:
                return head  # 没有k个直接返回
            node = node.next
            # node就是下一组的head了

        # 将后面的反转，并且找到头
        prev = self.reverseKGroup(node, k)

        # 反转当前组，将其添加到prev之前
        for _ in range(k):
            head.next, prev, head = prev, head, head.next

        # prev已经退到新的头
        return prev


    def reverseKGroup(self, root, k):
        if k <= 1:
            return root
        dummy = ListNode(0)
        dummy.next = root
        pre, cur = dummy, root
        while True:
            _k = k
            cur_k = cur
            while _k > 0 and cur_k:
                cur_k = cur_k.next
                _k -= 1
            if _k > 0:
                return dummy.next


            nc = cur.next
            while nc is not cur_k:
                nc.next, nc, cur = cur, nc.next, nc

            pre.next.next, pre.next, cur, pre = cur_k, cur, cur_k, pre.next

