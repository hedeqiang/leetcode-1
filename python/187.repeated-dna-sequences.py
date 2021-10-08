#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#
# https://leetcode-cn.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (48.46%)
# Total Accepted:    51.6K
# Total Submissions: 103.2K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# 所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA
# 中的重复序列有时会对研究非常有帮助。
#
# 编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。
#
#
#
# 示例 1：
#
#
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC","CCCCCAAAAA"]
#
#
# 示例 2：
#
#
# 输入：s = "AAAAAAAAAAAAA"
# 输出：["AAAAAAAAAA"]
#
#
#
#
# 提示：
#
#
# 0
# s[i] 为 'A'、'C'、'G' 或 'T'

from typing import List
from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences0(self, s: str) -> List[str]:
        counter = defaultdict(int)
        for i in range(len(s) - 10 + 1):
            sub_str = s[i : i + 10]
            counter[sub_str] += 1
        return [k for k in counter if counter[k] > 1]

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n, L, x = len(s), 10, 0
        if n < L:
            return []
        ch_map = dict(A=0b00, G=0b01, C=0b10, T=0b11)
        counter = defaultdict(int)
        ans = []
        for ch in s[0:L - 1]:
            x = (x << 2) | ch_map[ch]
        for i in range(L - 1, n):
            x = (x << 2 | ch_map[s[i]]) % 2 ** 20
            counter[x] += 1
            if counter[x] == 2:
                ans.append(s[i - L + 1 : i + 1])
        return ans


if __name__ == "__main__":
    Solution().findRepeatedDnaSequences("AAAAAAAAAAA")
