# [389] 找不同

# https://leetcode-cn.com/problems/find-the-difference/description/

# * algorithms
# * Easy (64.19%)
# * Total Accepted:    55.1K
# * Total Submissions: 81.9K
# * Testcase Example:  '"abcd"\n"abcde"'

# 给定两个字符串 s 和 t，它们只包含小写字母。

# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

# 请找出在 t 中被添加的字母。

#

# 示例 1：

# 输入：s = "abcd", t = "abcde"
# 输出："e"
# 解释：'e' 是那个被添加的字母。


# 示例 2：

# 输入：s = "", t = "y"
# 输出："y"


# 示例 3：

# 输入：s = "a", t = "aa"
# 输出："a"


# 示例 4：

# 输入：s = "ae", t = "aea"
# 输出："a"


#

# 提示：


# 	0 <= s.length <= 1000
# 	t.length == s.length + 1
# 	s 和 t 只包含小写字母


class Solution(object):
    def findTheDifference0(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sum_s = sum_t = 0
        for c in s:
            sum_s += ord(c)
        for c in t:
            sum_t += ord(c)
        return chr(sum_t - sum_s)

    def findTheDifference(self, s, t):
        ans = ord(t[-1])
        for i in range(len(s)):
            ans ^= ord(s[i])
            ans ^= ord(t[i])
        return chr(ans)
