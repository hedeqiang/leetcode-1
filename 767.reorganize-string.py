# [767] Reorganize String

# https://leetcode-cn.com/problems/reorganize-string/description/

# * algorithms
# * Medium (45.11%)
# * Total Accepted:    16.4K
# * Total Submissions: 36.5K
# * Testcase Example:  '"aab"'

# 给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。

# 若可行，输出任意可行的结果。若不可行，返回空字符串。

# 示例 1:


# 输入: S = "aab"
# 输出: "aba"


# 示例 2:


# 输入: S = "aaab"
# 输出: ""


# 注意:


# 	S 只包含小写字母并且长度在[1, 500]区间内。

from collections import Counter
import heapq


class Solution(object):
    # Timeout
    # def reorganizeString(self, S):
    #     # def dfs(prev, avail):
    #     #     print(prev, avail)
    #     #     if not avail:
    #     #         return prev
    #     #     for i, c in enumerate(avail):
    #     #         if not prev or prev[-1] != c:
    #     #             ans = dfs(prev+c, avail[:i]+avail[i+1:])
    #     #             if ans:
    #     #                 return ans
    #     #     return ""

    #     def dfs(prev, avail):
    #         print(prev, avail)
    #         if not avail:
    #             return prev
    #         for i, c in enumerate(avail):
    #             if not prev or prev[-1] != c:
    #                 ans = dfs(prev+c, avail[:i]+avail[i+1:])
    #                 if ans:
    #                     return ans
    #         return ""

    #     return dfs("", S)

    def reorganizeString(self, S):
        length = len(S)
        if length < 2:
            return S

        counter = Counter(S)
        max_count = counter.most_common(1)[0][1]
        if max_count > (length + 1) // 2:
            return ""

        # defaults to minheap
        queue = [(-x[1], x[0]) for x in counter.items()]
        heapq.heapify(queue)
        ans = []

        # pick the most most common 2 elements
        while len(queue) > 1:
            _, c1 = heapq.heappop(queue)
            _, c2 = heapq.heappop(queue)
            ans.extend([c1, c2])
            counter[c1] -= 1
            counter[c2] -= 1

            # put the rest back into the heap
            if counter[c1] > 0:
                heapq.heappush(queue, (-counter[c1], c1))

            if counter[c2] > 0:
                heapq.heappush(queue, (-counter[c2], c2))

        # append the last element when the elements number is odd
        if queue:
            ans.append(queue[0][1])

        return "".join(ans)


    def reorganizeString0(self, S):
        length = len(S)
        if length <= 2:
            return S
        counter = Counter(S)
        max_count = counter.most_common(1)[0][1]
        # 最多只能有 (n+1)/2 个相同元素
        if max_count > (length + 1) // 2:
            return ""

        even_index = 0
        odd_index = 1
        half_length = length // 2
        ans = [""] * length

        for char, count in counter.items():
            # 少于 (n+1)/2 的元素，先放到奇数位置
            while count > 0 and count <= half_length and odd_index < length:
                ans[odd_index] = char
                count -= 1
                odd_index += 2
            # 唯一最大的相同数目为 (n+1)/2 的元素，或者奇数位置放不下的元素，放到偶数坐标
            while count > 0:
                ans[even_index] = char
                count -= 1
                even_index += 2

        return "".join(ans)


# res = Solution().reorganizeString("bbbbaaaaababaababab")
# print(res)
