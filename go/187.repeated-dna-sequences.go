/*
 * @lc app=leetcode.cn id=187 lang=golang
 *
 * [187] 重复的DNA序列
 *
 * https://leetcode-cn.com/problems/repeated-dna-sequences/description/
 *
 * algorithms
 * Medium (48.46%)
 * Total Accepted:    51.6K
 * Total Submissions: 103.2K
 * Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
 *
 * 所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA
 * 中的重复序列有时会对研究非常有帮助。
 *
 * 编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
 * 输出：["AAAAACCCCC","CCCCCAAAAA"]
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "AAAAAAAAAAAAA"
 * 输出：["AAAAAAAAAA"]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0
 * s[i] 为 'A'、'C'、'G' 或 'T'
 *
 *
 */

// package main

const L = 10

var bin = map[byte]int{'A': 0b00, 'C': 0b01, 'G': 0b10, 'T': 0b11}

func findRepeatedDnaSequences(s string) (ans []string) {
	n := len(s)
	if n < L {
		return
	}
	x := 0
	for _, ch := range s[:L-1] {
		x = (x << 2) | bin[byte(ch)]
	}
	cnt := map[int]int{}
	for i := L - 1; i < n; i++ {
		x = (x<<2 | bin[byte(s[i])]) & (1<<(L*2) - 1)
		cnt[x]++
		if cnt[x] == 2 {
			ans = append(ans, s[i-L+1:i+1])
		}
	}
	return
}
