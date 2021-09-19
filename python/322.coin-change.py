# coding: utf-8
# [322] 零钱兑换

# https://leetcode-cn.com/problems/coin-change/description/

# * algorithms
# * Medium (41.70%)
# * Total Accepted:    147.2K
# * Total Submissions: 352.9K
# * Testcase Example:  '[1,2,5]\n11'

# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

# 你可以认为每种硬币的数量是无限的。

#

# 示例 1：


# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1

# 示例 2：


# 输入：coins = [2], amount = 3
# 输出：-1

# 示例 3：


# 输入：coins = [1], amount = 0
# 输出：0


# 示例 4：


# 输入：coins = [1], amount = 1
# 输出：1


# 示例 5：


# 输入：coins = [1], amount = 2
# 输出：2


#

# 提示：


# 	1
# 	1
# 	0


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        # F(amount) = F(amount - coin) + 1
        # 其中F(amount-coin)初始值为无穷大，无穷大+1还是无穷大
        # 每个coin面值、每个amount情况，都对F()做了min比较取值
        # 最后能直接出结果
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1
