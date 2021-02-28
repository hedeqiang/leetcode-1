# [896] 单调数组

# https://leetcode-cn.com/problems/monotonic-array/description/

# * algorithms
# * Easy (53.98%)
# * Total Accepted:    49.4K
# * Total Submissions: 84.5K
# * Testcase Example:  '[1,2,2,3]'

# 如果数组是单调递增或单调递减的，那么它是单调的。

# 如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。

# 当给定的数组 A 是单调数组时返回 true，否则返回 false。

# 示例 1：

# 输入：[1,2,2,3]
# 输出：true


# 示例 2：

# 输入：[6,5,4,4]
# 输出：true


# 示例 3：

# 输入：[1,3,2]
# 输出：false


# 示例 4：

# 输入：[1,2,4,5]
# 输出：true


# 示例 5：

# 输入：[1,1,1]
# 输出：true

# 提示：

# 	1 <= A.length <= 50000
# 	-100000 <= A[i] <= 100000


class Solution:
    def isMonotonic0(self, a):
        n = len(a)
        if n <= 2:
            return True
        flag = None
        for i in range(1, n):
            if a[i - 1] != a[i]:
                if flag is None:
                    flag = a[i - 1] > a[i]
                elif flag != (a[i - 1] > a[i]):
                    return False
        return True

    def isMonotonic1(self, a):
        desc = True if a[0] >= a[-1] else False
        n = len(a)
        if desc:
            return all(a[i - 1] >= a[i] for i in range(1, n))
        return all(a[i - 1] <= a[i] for i in range(1, n))

    def isMonotonic(self, a):
        asc, desc = True, True
        i, n = 1, len(a)
        while i < n and (asc or desc):
            asc = asc and a[i - 1] <= a[i]
            desc = desc and a[i - 1] >= a[i]
            i += 1
        return asc or desc
