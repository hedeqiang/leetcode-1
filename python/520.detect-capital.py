#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#
# https://leetcode-cn.com/problems/detect-capital/description/
#
# algorithms
# Easy (56.27%)
# Total Accepted:    61.8K
# Total Submissions: 107.4K
# Testcase Example:  '"USA"'
#
# 我们定义，在以下情况时，单词的大写用法是正确的：
#
#
# 全部字母都是大写，比如 "USA" 。
# 单词中所有字母都不是大写，比如 "leetcode" 。
# 如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。
#
#
# 给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。
#
# 示例 1：
#
# 输入：word = "USA"
# 输出：true
#
# 示例 2：
#
# 输入：word = "FlaG"
# 输出：false
#
# 提示：
#
# 1 <= word.length <= 100
# word 由小写和大写英文字母组成


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) >= 2 and word[0].islower() and word[1].isupper():
            return False

        for i in range(2, len(word)):
            if word[1].islower() != word[i].islower():
                return False

        return True
