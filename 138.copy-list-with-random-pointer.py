#
# @lc app=leetcode.cn id=138 lang=python
#
# [138] 复制带随机指针的链表
#
# https://leetcode-cn.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (25.54%)
# Total Accepted:    6K
# Total Submissions: 20.5K
# Testcase Example:  '{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}'
#
# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
# 
# 要求返回这个链表的深拷贝。 
# 
# 
# 
# 示例：
# 
# 
# 
# 输入：
# 
# {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
# 
# 解释：
# 节点 1 的值是 1，它的下一个指针和随机指针都指向节点 2 。
# 节点 2 的值是 2，它的下一个指针指向 null，随机指针指向它自己。
# 
# 
# 
# 
# 提示：
# 
# 
# 你必须返回给定头的拷贝作为对克隆列表的引用。
# 
# 
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

from copy import deepcopy


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        # 顺序复制，并插入原节点后面
        cur = head
        while cur:
            node = Node(cur.val, None, None)
            node.next = cur.next
            cur.next = node
            cur = cur.next.next

        cur = head
        while cur:
            if cur.random:
                # 当前节点的random指向的位置，也被复制到指向位置后一个了
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 分裂复制的节点链表
        new_head = head.next
        p_old = head
        p_new = new_head
        while p_new.next:
            # 老链表顺序后移
            p_old.next = p_new.next
            p_old = p_old.next

            # 新链表顺序后移
            p_new.next = p_old.next
            p_new = p_new.next

        p_old.next = None

        return new_head

