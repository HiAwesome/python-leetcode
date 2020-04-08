"""
https://leetcode-cn.com/problems/clone-graph/
https://leetcode-cn.com/problems/clone-graph/solution/ke-long-tu-by-leetcode/
https://leetcode-cn.com/problems/clone-graph/solution/dfs-he-bfs-by-powcai/
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        if neighbors is None:
            neighbors = []
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: Node) -> Node:

        lookup = {}

        def dfs(node):
            if not node:
                return

            if node in lookup:
                return lookup[node]

            clone = Node(node.val, [])
            lookup[node] = clone

            for n in node.neighbors:
                clone.neighbors.append(dfs(n))

            return clone

        return dfs(node)
