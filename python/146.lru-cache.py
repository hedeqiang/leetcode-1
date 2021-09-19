#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (44.80%)
# Total Accepted:    27.6K
# Total Submissions: 61.5K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
#
# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) -
# 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。
#
# 进阶:
#
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？
#
# 示例:
#
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4


import collections


class ListNode:
    def __init__(self, key, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    def __init__(self):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, key, value):
        node = ListNode(key, value, prev=self.tail.prev, next=self.tail)
        self.tail.prev.next = node
        self.tail.prev = node

    def move_to_head(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def prepend(self, key, value):
        node = ListNode(key, value, prev=self.head, next=self.head.next)
        self.head.next.prev = node
        self.head.next = node

    def pop(self):
        if self.head.next == self.tail:
            raise IndexError('Pop from empty list')
        node = self.tail.prev
        prev = self.tail.prev.prev
        prev.next = self.tail
        self.tail.prev = prev
        return node


class LRUCache2:

    def __init__(self, capacity: int):
        self.key_node_map = {}
        self.size = capacity
        self.cache = DoubleLinkedList()

    def get(self, key: int) -> int:
        node = self.key_node_map.get(key)
        if not node:
            return -1
        self.cache.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.key_node_map:
            node = self.key_node_map[key]
            node.value = value
            self.cache.move_to_head(node)
            return
        if len(self.key_node_map) >= self.size:
            node = self.cache.pop()
            self.key_node_map.pop(node.key)
        self.cache.prepend(key, value)
        self.key_node_map[key] = self.cache.head.next


class LRUCache:
    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v   # set key as the newest one
        return v

    def put(self, key, value):
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:  # self.dic is full
                # last = False, FIFO; last = True, LIFO
                self.dic.popitem(last=False)
        self.dic[key] = value
