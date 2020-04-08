"""
https://leetcode-cn.com/problems/target-sum/
https://leetcode-cn.com/problems/target-sum/solution/mu-biao-he-by-leetcode/
https://leetcode-cn.com/problems/target-sum/solution/python-dfs-xiang-jie-by-jimmy00745/
"""
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dic = {}

        def dfs(cur, i, d):
            if i < len(nums) and (cur, i) not in dic:  # 搜索周围节点
                dic[(cur, i)] = dfs(cur + nums[i], i + 1, d) + dfs(cur - nums[i], i + 1, d)
            return dic.get((cur, i), int(cur == S))

        return dfs(0, 0, dic)
