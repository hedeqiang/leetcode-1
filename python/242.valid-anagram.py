# [242] 有效的字母异位词

# https://leetcode-cn.com/problems/valid-anagram/description/

# * algorithms
# * Easy (61.76%)
# * Total Accepted:    147.7K
# * Total Submissions: 239.1K
# * Testcase Example:  '"anagram"\n"nagaram"'

# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

# 示例 1:

# 输入: s = "anagram", t = "nagaram"
# 输出: true


# 示例 2:

# 输入: s = "rat", t = "car"
# 输出: false

# 说明:
# 你可以假设字符串只包含小写字母。

# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？


class Solution(object):
    def isAnagram1(self, s, t):
        return sorted(s) == sorted(t)

    def isAnagram(self, s, t):
        d = {}
        for x in s:
            d[x] = d.get(x, 0) + 1
        for x in t:
            d[x] = d.get(x, 0) - 1

        return all([x == 0 for x in d.values()])

        # for v in d.values():
        #     if v != 0:
        #         return False
        # return True
