# [738] 单调递增的数字

# https://leetcode-cn.com/problems/monotone-increasing-digits/description/

# * algorithms
# * Medium (44.34%)
# * Total Accepted:    8K
# * Total Submissions: 17.5K
# * Testcase Example:  '10'

# 给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。

# （当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

# 示例 1:

# 输入: N = 10
# 输出: 9


# 示例 2:

# 输入: N = 1234
# 输出: 1234


# 示例 3:

# 输入: N = 332
# 输出: 299


# 说明: N 是在 [0, 10^9] 范围内的一个整数。


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        digits = []
        d = N
        while d > 0:
            digits.append(d % 10)
            d //= 10
        digits.reverse()

        # 就个位数
        length = len(digits)
        if length == 1:
            return d

        i = 1
        while i < length:
            if digits[i] < digits[i - 1]:
                break
            i += 1

        # 本来就是单调递增的
        if i == length:
            return N

        # 跟不递增的前一个数字一样的，都要-1
        while i > 1 and digits[i - 1] == digits[i - 2]:
            i -= 1

        digits[i - 1] -= 1
        digits[i:] = [9] * (length - i)

        # 可以去掉前面的0
        return int("".join(map(str, digits)))
