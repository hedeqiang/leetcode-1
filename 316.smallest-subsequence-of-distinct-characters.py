# [316] 去除重复字母

# https://leetcode-cn.com/problems/remove-duplicate-letters/description/

# * algorithms
# * Medium (43.28%)
# * Total Accepted:    26.5K
# * Total Submissions: 61.3K
# * Testcase Example:  '"bcabc"'

# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

# 注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters 相同

#

# 示例 1：


# 输入：s = "bcabc"
# 输出："abc"


# 示例 2：


# 输入：s = "cbacdcbc"
# 输出："acdb"

#

# 提示：


# 	1
# 	s 由小写英文字母组成


class Solution(object):
    def removeDuplicateLetters(self, s):
        # 记录最后一个位置，作为判断是会否要丢掉的依据
        rindex = {c: i for i, c in enumerate(s)}
        result = ''
        for i, c in enumerate(s):
            if c not in result:
                # 栈顶大了，且后面还有
                while c < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]
                result += c
        return result
