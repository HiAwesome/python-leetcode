"""
https://leetcode-cn.com/problems/generate-parentheses/
https://leetcode-cn.com/problems/generate-parentheses/solution/gua-hao-sheng-cheng-by-leetcode-solution/
"""
from functools import lru_cache
from typing import List


class Solution:

    @lru_cache(None)
    def generateParenthesis(self, m: int) -> List[str]:
        if m == 0:
            return ['']

        ans = []

        for c in range(m):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(m - 1 - c):
                    ans.append('({}){}'.format(left, right))

        return ans
