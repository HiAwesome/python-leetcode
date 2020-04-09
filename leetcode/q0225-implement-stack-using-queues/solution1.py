"""
https://leetcode-cn.com/problems/implement-stack-using-queues/
https://leetcode-cn.com/problems/implement-stack-using-queues/solution/yong-dui-lie-shi-xian-zhan-by-leetcode/
https://leetcode-cn.com/problems/implement-stack-using-queues/solution/python3-list-dequeshi-xian-by-xilepeng/
"""


class MyStack:

    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

        for i in range(len(self.data), 1, -1):
            # 反转前面 n-1 个元素，栈顶元素始终保留在队首
            self.data.append(self.data.pop(0))

    def pop(self) -> int:
        return self.data.pop(0)

    def top(self) -> int:
        return self.data[0]

    def empty(self) -> bool:
        return not bool(self.data)
