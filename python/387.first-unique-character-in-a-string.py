# [387] 字符串中的第一个唯一字符

# https://leetcode-cn.com/problems/first-unique-character-in-a-string/description/

# * algorithms
# * Easy (48.00%)
# * Total Accepted:    135.6K
# * Total Submissions: 270.5K
# * Testcase Example:  '"leetcode"'

# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

#

# 示例：

# s = "leetcode"
# 返回 0

# s = "loveleetcode"
# 返回 2


#

# 提示：你可以假定该字符串只包含小写字母。

# from collections import OrderedDict

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # lookup = OrderedDict()
        lookup = {}
        for i, c in enumerate(s):
            if c in lookup:
                lookup[c] = -1
            else:
                lookup[c] = i

        ans = n

        for x in lookup.values():
            if x != -1 and x < ans:
                ans = x

        if ans == n:
            ans = -1

        return ans

        # for v in lookup.values():
        #     if v != -1:
        #         return v

        # return -1


    def firstUniqChar2(self, s):
        lookup = [0] * 26
        for c in s:
            lookup[ord(c) - 97] += 1

        for i in range(len(s)):
            if lookup[ord(s[i]) - 97] == 1:
                return i
        return -1
