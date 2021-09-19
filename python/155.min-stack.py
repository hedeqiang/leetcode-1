#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
# https://leetcode-cn.com/problems/min-stack/description/
#
# algorithms
# Easy (50.76%)
# Total Accepted:    62.3K
# Total Submissions: 122.7K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n' +
# '[[],[-2],[0],[-3],[],[],[],[]]'
#
# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
#
#
# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。
#
#
# 示例:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#
#
#


class MinStack0:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []
        self.mins = []

    def push(self, x: int) -> None:
        self.values.append(x)
        if not len(self.mins):
            self.mins.append(x)
        else:
            self.mins.append(min(x, self.mins[-1]))

    def pop(self) -> None:
        self.mins.pop()
        return self.values.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.mins[-1]

        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()


class MinStack:
    def __init__(self):
        self.s = []

    def push(self, x):
        if not len(self.s):
            self.s.append(x)
            self.s.append(x)
        else:
            v = min(self.getMin(), x)
            self.s.append(x)
            self.s.append(v)

    def pop(self):
        self.s.pop()
        return self.s.pop()

    def top(self):
        return self.s[-2]

    def getMin(self):
        return self.s[-1]
