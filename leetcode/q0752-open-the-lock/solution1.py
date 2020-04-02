"""
https://leetcode-cn.com/problems/open-the-lock/
https://leetcode-cn.com/problems/open-the-lock/solution/da-kai-zhuan-pan-suo-by-leetcode/
https://leetcode-cn.com/problems/open-the-lock/solution/python-bfs-qing-xi-ti-jie-by-knifezhu/
"""
import collections
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(base_node):
            for i in range(4):
                x = int(base_node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield base_node[:i] + str(y) + base_node[i + 1:]

        dead = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}

        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            if node in dead:
                continue
            for neighbor in neighbors(node):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, depth + 1))

        return -1
