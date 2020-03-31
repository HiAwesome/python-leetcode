"""
https://leetcode-cn.com/problems/number-of-islands/
https://leetcode-cn.com/problems/number-of-islands/solution/dao-yu-shu-liang-by-leetcode/
https://leetcode-cn.com/problems/number-of-islands/solution/dfs-bfs-bing-cha-ji-python-dai-ma-java-dai-ma-by-l/
"""
from collections import deque
from typing import List


class Solution:
    """
              x-1, y
    x, y-1    x, y    x, y+1
              x+1, y
    方向数组，它表示了相对于当前位置的 4 个方向的横纵坐标的偏移量，是一个常见技巧
    """
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)

        if m == 0:
            return 0

        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):

                if not marked[i][j] and grid[i][j] == '1':
                    count += 1
                    queue = deque()
                    queue.append((i, j))
                    marked[i][j] = True

                    while queue:
                        cur_x, cur_y = queue.popleft()

                        for direction in self.directions:
                            new_i = cur_x + direction[0]
                            new_j = cur_y + direction[1]

                            if 0 <= new_i < m and 0 <= new_j < n \
                                    and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
                                queue.append((new_i, new_j))
                                marked[new_i][new_j] = True

        return count


if __name__ == '__main__':
    test_grid = [['1', '1', '1', '1', '0'],
                 ['1', '1', '0', '1', '0'],
                 ['1', '1', '0', '0', '0'],
                 ['0', '0', '0', '0', '0']]
    solution = Solution()
    result = solution.numIslands(test_grid)
    print(result)
