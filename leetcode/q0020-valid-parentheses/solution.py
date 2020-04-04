"""
https://leetcode-cn.com/problems/valid-parentheses/
https://leetcode-cn.com/problems/valid-parentheses/solution/you-xiao-de-gua-hao-by-leetcode/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in dic:
                top_element = stack.pop() if stack else ''
                if dic[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
