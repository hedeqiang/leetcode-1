# [567] 字符串的排列

# https://leetcode-cn.com/problems/permutation-in-string/description/

# * algorithms
# * Medium (41.09%)
# * Total Accepted:    69.9K
# * Total Submissions: 170.2K
# * Testcase Example:  '"ab"\n"eidbaooo"'

# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

# 换句话说，第一个字符串的排列之一是第二个字符串的子串。

# 示例1:
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").

# 示例2:
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False

# 注意：
# 	输入的字符串只包含小写字母
# 	两个字符串的长度都在 [1, 10,000] 之间

# from collections import Counter


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        N1, N2 = len(s1), len(s2)
        left, right = 0, N1-1
        counter1 = Counter(s1)
        counter2 = Counter(s2[:right])
        while right < N2:
            counter2[s2[right]] += 1

            if counter1 == counter2:
                return True

            counter2[s2[left]] -= 1
            if counter2[s2[left]] == 0:
                del counter2[s2[left]]
            left += 1
            right += 1

        return False
