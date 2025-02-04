"""
https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/ji-qi-ren-de-yun-dong-fan-wei-by-leetcode-solution/
https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/mian-shi-ti-13-ji-qi-ren-de-yun-dong-fan-wei-dfs-b/
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int):
        queue, visited = [(0, 0, 0, 0)], set()

        while queue:
            i, j, si, sj = queue.pop(0)

            if i >= m or j >= n or k < si + sj or (i, j) in visited:
                continue

            visited.add((i, j))
            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))

        return len(visited)
