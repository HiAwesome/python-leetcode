"""
https://leetcode-cn.com/problems/implement-stack-using-queues/
https://leetcode-cn.com/problems/implement-stack-using-queues/solution/yong-dui-lie-shi-xian-zhan-by-leetcode/
https://leetcode-cn.com/problems/implement-stack-using-queues/solution/python3-list-dequeshi-xian-by-xilepeng/
"""
from collections import deque


class MyStack:

    def __init__(self):
        self.data = deque()
        self.help = deque()

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        while len(self.data) > 1:
            self.help.append(self.data.popleft())

        tmp = self.data.popleft()
        self.help, self.data = self.data, self.help
        return tmp

    def top(self) -> int:
        while len(self.data) != 1:
            self.help.append(self.data.popleft())

        tmp = self.data.popleft()
        self.help.append(tmp)
        self.help, self.data = self.data, self.help
        return tmp

    def empty(self) -> bool:
        return not bool(self.data)
