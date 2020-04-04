"""
https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/
https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/solution/zhi-de-jie-jian-de-xie-fa-by-powcai/

"""
from typing import List


class Solution:
    def evalPRN(self, tokens: List[str]) -> int:
        stack = []
        opt = ['+', '-', '*', '/']

        for c in tokens:
            if c not in opt:
                stack.append(c)
            else:
                b = int(stack.pop())
                a = int(stack.pop())

                if c == '+':
                    stack.append(str(a + b))
                elif c == '-':
                    stack.append(str(a - b))
                elif c == '*':
                    stack.append(str(a * b))
                elif c == '/':
                    stack.append(str(int(a / b)))

        return int(stack[0])
