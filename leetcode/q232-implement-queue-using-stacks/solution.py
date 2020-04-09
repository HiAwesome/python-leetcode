"""
https://leetcode-cn.com/problems/implement-queue-using-stacks/
https://leetcode-cn.com/problems/implement-queue-using-stacks/solution/yong-zhan-shi-xian-dui-lie-by-leetcode/
https://leetcode-cn.com/problems/implement-queue-using-stacks/solution/bzhan-tu-jie-leetcode-232-yong-zhan-mo-ni-dui-lie-/
"""


class MyQueue:

    def __init__(self):
        self.a = []
        self.b = []

    def push(self, x: int) -> None:
        self.a.append(x)

    def pop(self) -> int:
        if not self.b:
            while self.a:
                self.b.append(self.a.pop())

        return self.b.pop()

    def peek(self) -> int:
        if not self.b:
            while self.a:
                self.b.append(self.a.pop())

        return self.b[-1]

    def empty(self) -> int:
        return not self.a and not self.b
