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
    def rotateRight0(self, head, k):
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

    def rotateRight(self, head, k):
        if not head:
            return head

        slow = fast = head
        i = 0
        while i < k:
            i += 1
            fast = fast.next
            if not fast:
                k = k % i
                i = 0
                fast = head

        # print(f"{slow.val=}, {fast.val=}")

        if slow == fast:
            return head

        while fast.next:
            slow = slow.next
            fast = fast.next
            # print(f"{slow.val=}, {fast.val=}")

        new_head = slow.next
        slow.next = None
        fast.next = head

        return new_head


def test():
    def init_list(items):
        dummy = ListNode(None)
        cur = dummy
        for x in items:
            cur.next = ListNode(x)
            cur = cur.next
        return dummy.next

    def print_list(head):
        tmp = []
        cur = head
        while cur:
            tmp.append(str(cur.val))
            cur = cur.next
        print("->".join(tmp))

    # for k in range(1, 11):
    #     print(f"{k=}")
    #     head = init_list(range(1, 6))
    #     print_list(head)
    #     new_head = Solution().rotateRight(head, k)
    #     print_list(new_head)
    #     print("-" * 10)

    # head = init_list([1,2,3])
    # new_head = Solution().rotateRight(head, 20000)
    # print_list(new_head)


# test()
