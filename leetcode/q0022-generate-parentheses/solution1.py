"""
https://leetcode-cn.com/problems/generate-parentheses/
https://leetcode-cn.com/problems/generate-parentheses/solution/gua-hao-sheng-cheng-by-leetcode-solution/
"""
from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backstrack(line, left, right):
            if len(line) == 2 * n:
                ans.append(''.join(line))
                return

            if left < n:
                line.append('(')
                backstrack(line, left + 1, right)
                line.pop()

            if right < left:
                line.append(')')
                backstrack(line, left, right + 1)
                line.pop()

        backstrack([], 0, 0)

        return ans
