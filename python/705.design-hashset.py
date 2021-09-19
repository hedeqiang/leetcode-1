#!/usr/bin/env python3
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] Design HashSet
#
# https://leetcode-cn.com/problems/design-hashset/description/
#
# algorithms
# Easy (58.81%)
# Total Accepted:    36.8K
# Total Submissions: 58.5K
# Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n' +  '[[],[1],[2],[1],[3],[2],[2],[2],[2]]'
#
# 不使用任何内建的哈希表库设计一个哈希集合（HashSet）。
#
# 实现 MyHashSet 类：
#
#
# void add(key) 向哈希集合中插入值 key 。
# bool contains(key) 返回哈希集合中是否存在这个值 key 。
# void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
# 示例：

# 输入：
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains",
# "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# 输出：
# [null, null, null, true, false, null, true, null, false]

# 解释：
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // 返回 True
# myHashSet.contains(3); // 返回 False ，（未找到）
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // 返回 True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // 返回 False ，（已移除）

# 提示：
# 最多调用 10^4 次 add、remove 和 contains 。
# 进阶：你可以不使用内建的哈希集合库解决此问题吗？
#


class MyHashSet1:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [False] * (10 ** 6 + 1)

    def add(self, key: int) -> None:
        self.arr[key] = True

    def remove(self, key: int) -> None:
        self.arr[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.arr[key]


class MyHashSet2:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.items_per_bucket = 1001
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key: int) -> int:
        return key % self.buckets

    def pos(self, key: int) -> int:
        return key // self.buckets

    def add(self, key: int) -> None:
        hashkey = self.hash(key)
        if not self.table[hashkey]:
            self.table[hashkey] = [0] * self.items_per_bucket
        self.table[hashkey][self.pos(key)] = 1

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        if self.table[hashkey]:
            self.table[hashkey][self.pos(key)] = 0

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashkey = self.hash(key)
        return (self.table[hashkey] != []) and (self.table[hashkey][self.pos(key)] == 1)


class MyHashSet:
    def __init__(self):
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key: int) -> int:
        return key % self.buckets

    def add(self, key: int) -> None:
        hashkey = self.hash(key)
        if key in self.table[hashkey]:
            return
        self.table[hashkey].append(key)

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        if key not in self.table[hashkey]:
            return
        self.table[hashkey].remove(key)

    def contains(self, key: int) -> bool:
        hashkey = self.hash(key)
        return key in self.table[hashkey]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
