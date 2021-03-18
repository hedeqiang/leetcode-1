#!/usr/bin/env python3
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (52.42%)
# Total Accepted:    125.5K
# Total Submissions: 235.1K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 给你单链表的头节点 head 和两个整数 left 和 right ，其中 left  。请你反转从位置 left 到位置 right 的链表节点，返回
# 反转后的链表 。
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#
#
# 示例 2：
#
#
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
#
#
#
#
# 提示：
#
#
# 链表中节点数目为 n
# 1
# -500
# 1
#
#
#
#
# 进阶： 你可以使用一趟扫描完成反转吗？
#
#
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"<Node {self.val}>"


# def print_linklist(head):
#     cur = head
#     ret = []
#     while cur:
#         ret.append(cur.val)
#         cur = cur.next
#     print("->".join(map(str, ret)))


# def init_linklist(n):
#     dummy = ListNode(val=None)
#     cur = dummy
#     for i in range(1, n+1):
#         node = ListNode(i)
#         cur.next = node
#         cur = cur.next
#     return dummy.next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        pre_left = node_left = None
        pre, cur = dummy, head
        num = 0

        while cur and num <= right:
            num += 1
            if num == left:
                pre_left = pre
                node_left = cur
            elif num > left:
                pre, cur.next, cur = cur, pre, cur.next
            else:
                pre, cur = cur, cur.next
        pre_left.next, node_left.next = pre, cur
        return dummy.next
