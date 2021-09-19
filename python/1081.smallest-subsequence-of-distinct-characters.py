# [1081] 不同字符的最小子序列

# https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters/description/

# * algorithms
# * Medium (53.88%)
# * Total Accepted:    6.7K
# * Total Submissions: 12.5K
# * Testcase Example:  '"bcabc"'

# 返回字符串 text 中按字典序排列最小的子序列，该子序列包含 text 中所有不同字符一次。

#

# 示例 1：

# 输入："cdadabcc"
# 输出："adbc"


# 示例 2：

# 输入："abcd"
# 输出："abcd"


# 示例 3：

# 输入："ecbacba"
# 输出："eacb"


# 示例 4：

# 输入："leetcode"
# 输出："letcod"


#

# 提示：


# 	1 <= text.length <= 1000
# 	text 由小写英文字母组成


#

# 注意：本题目与 316 https://leetcode-cn.com/problems/remove-duplicate-letters/ 相同

import collections


class Solution(object):
    def smallestSubsequence(self, text):
        seen = set()
        stack = []
        # 记录每个字母还可以删除几次，也可以保存每个字符最右边的位置用于判断
        remain_counter = collections.Counter(text)
        for c in text:
            # 每个字母只能出现一次，之前出现过的，现在没有出现过的意义，这是一个单调递增的栈
            if c not in seen:
                # 栈顶太大了，而且后面还有
                while stack and stack[-1] > c and remain_counter[stack[-1]] > 0:
                    seen.discard(stack.pop())
                stack.append(c)
                seen.add(c)
            remain_counter[c] -= 1
        return "".join(stack)
