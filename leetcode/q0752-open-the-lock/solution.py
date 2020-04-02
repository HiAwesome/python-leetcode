"""
https://leetcode-cn.com/problems/open-the-lock/
https://leetcode-cn.com/problems/open-the-lock/solution/da-kai-zhuan-pan-suo-by-leetcode/
https://leetcode-cn.com/problems/open-the-lock/solution/python-bfs-qing-xi-ti-jie-by-knifezhu/
"""
from queue import Queue
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # in 操作在 set 中时间复杂度为 O(1)
        deadends = set(deadends)
        if '0000' in deadends:
            return -1

        q = Queue()
        q.put(('0000', 0))

        while not q.empty():
            node, step = q.get()

            for i in range(4):
                for add in (1, -1):
                    cur = node[:i] + str((int(node[i]) + add) % 10) + node[i + 1:]
                    if cur == target:
                        return step + 1
                    if cur not in deadends:
                        q.put((cur, step + 1))
                        deadends.add(cur)

        return -1
