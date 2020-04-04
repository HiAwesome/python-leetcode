"""
https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/
https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/solution/zhi-de-jie-jian-de-xie-fa-by-powcai/

"""
from typing import List


class Solution:
    def evalPRN(self, tokens: List[str]) -> int:
        stack = []
        plus = lambda a, b: b + a
        sub = lambda a, b: b - a
        mul = lambda a, b: b * a
        div = lambda a, b: int(b / a)

        opt = {'+': plus, '-': sub, '*': mul, '/': div}

        for t in tokens:
            if t in opt:
                stack.append(opt[t](stack.pop(), stack.pop()))
            else:
                stack.append(int(t))

        return stack.pop()
