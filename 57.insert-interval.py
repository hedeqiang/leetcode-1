# [57] 插入区间

# https://leetcode-cn.com/problems/insert-interval/description/

# * algorithms
# * Hard (38.02%)
# * Total Accepted:    34K
# * Total Submissions: 88.7K
# * Testcase Example:  '[[1,3],[6,9]]\n[2,5]'

# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。

# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

# 示例 1：

# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]


# 示例 2：

# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。


# 注意：输入类型已在 2019 年 4 月 15 日更改。请重置为默认代码定义以获取新的方法签名。


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        inserted = False
        l, r = newInterval

        for li, ri in intervals:
            # print('🧐', l, r)
            if li > r:
                # 右边，无交集
                if not inserted:
                    res.append([l, r])
                    inserted = True
                res.append([li, ri])
            elif ri < l:
                # 左边，无交集
                res.append([li, ri])
            else:
                # 重叠，合并
                l = min(l, li)
                r = max(r, ri)
            # print('📜', res)
            # print()

        if not inserted:
            res.append([l, r])
        # print('👐', res)
        return res

# Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8])

# 🧐 4 8
# 📜 [[1, 2]]

# 🧐 4 8
# 📜 [[1, 2]]

# 🧐 3 8
# 📜 [[1, 2]]

# 🧐 3 8
# 📜 [[1, 2]]

# 🧐 3 10
# 📜 [[1, 2], [3, 10], [12, 16]]

# 👐 [[1, 2], [3, 10], [12, 16]]
