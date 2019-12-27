#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (36.80%)
# Total Accepted:    103.7K
# Total Submissions: 281.8K
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


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        left, right = head, head
        # 先走n步
        for _ in range(n):
            right = right.next

        # 因为假设n一定对，所以right到头
        # 则刚好走了n步，倒数第n个节点就是head
        # 删除head，就返回head之后的节点
        # 否则n一定小于长度，head一定不是倒数第n个
        if not right:
            return head.next

        # 同时往前走，right过头、left就就为倒数第n了
        # 需要找到倒数第n+1，才能方便删除倒数第n
        # 那right正好到头即可
        while right.next:
            right = right.next
            left = left.next
        left.next = left.next.next
        return head
