/*
 * @lc app=leetcode.cn id=650 lang=golang
 *
 * [650] 只有两个键的键盘
 *
 * https://leetcode-cn.com/problems/2-keys-keyboard/description/
 *
 * algorithms
 * Medium (53.61%)
 * Total Accepted:    29.3K
 * Total Submissions: 53.9K
 * Testcase Example:  '3'
 *
 * 最初记事本上只有一个字符 'A' 。你每次可以对这个记事本进行两种操作：
 *
 *
 * Copy All（复制全部）：复制这个记事本中的所有字符（不允许仅复制部分字符）。
 * Paste（粘贴）：粘贴 上一次 复制的字符。
 *
 *
 * 给你一个数字 n ，你需要使用最少的操作次数，在记事本上输出 恰好 n 个 'A' 。返回能够打印出 n 个 'A' 的最少操作次数。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：3
 * 输出：3
 * 解释：
 * 最初, 只有一个字符 'A'。
 * 第 1 步, 使用 Copy All 操作。
 * 第 2 步, 使用 Paste 操作来获得 'AA'。
 * 第 3 步, 使用 Paste 操作来获得 'AAA'。
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 1
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 1000
 *
 *
 */

package main

import "math"

func minSteps(n int) int {
	f := make([]int, n+1)
	for i := 2; i <= n; i++ {
		f[i] = math.MaxInt32
		for j := 1; j*j <= i; j++ {
			if i%j == 0 {
				f[i] = min(f[i], f[j]+i/j)
				f[i] = min(f[i], f[i/j]+j)
			}
		}
	}
	return f[n]
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}
