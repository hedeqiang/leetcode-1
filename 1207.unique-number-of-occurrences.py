# [1207] 独一无二的出现次数

# https://leetcode-cn.com/problems/unique-number-of-occurrences/description/

# * algorithms
# * Easy (69.66%)
# * Total Accepted:    34.1K
# * Total Submissions: 46.2K
# * Testcase Example:  '[1,2,2,1,1,3]'

# 给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。

# 如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。

#

# 示例 1：

# 输入：arr = [1,2,2,1,1,3]
# 输出：true
# 解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。

# 示例 2：

# 输入：arr = [1,2]
# 输出：false


# 示例 3：

# 输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]
# 输出：true


#

# 提示：


# 	1 <= arr.length <= 1000
# 	-1000 <= arr[i] <= 1000


class Solution(object):
    def uniqueOccurrences0(self, arr):
        from collections import Counter

        ct = Counter(arr)
        ct2 = Counter(ct.values())
        return ct2.most_common(1)[0][1] == 1

    def uniqueOccurrences1(self, arr):
        dt = {}
        cnts = set()
        for x in arr:
            dt[x] = dt.get(x, 0) + 1
        for x in dt.values():
            if x in cnts:
                return False
            cnts.add(x)
        return True

    def uniqueOccurrences2(self, arr):
        arr.sort()
        cnt = 1
        cnts = set()
        pre = arr[0]
        for x in arr[1:]:
            if x == pre:
                cnt += 1
            else:
                if cnt in cnts:
                    return False
                cnts.add(cnt)
                cnt = 1
                pre = x

        if cnt in cnts:
            return False

        return True


# res = Solution().uniqueOccurrences([1, 2])
# print(res)
