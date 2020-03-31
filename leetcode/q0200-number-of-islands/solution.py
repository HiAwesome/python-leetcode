"""
https://leetcode-cn.com/problems/number-of-islands/
https://leetcode-cn.com/problems/number-of-islands/solution/dao-yu-shu-liang-by-leetcode/
https://leetcode-cn.com/problems/number-of-islands/solution/dfs-bfs-bing-cha-ji-python-dai-ma-java-dai-ma-by-l/
"""
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
        row_length = len(grid)

        if row_length == 0:
            return 0

        column_length = len(grid[0])
        marked = [[False for _ in range(column_length)] for _ in range(row_length)]
        count = 0
        # 从第一行第一格开始，对每一格尝试进行一次 dfs 操作
        for i in range(row_length):
            for j in range(column_length):
                # 只要是陆地，且没有被访问过，就可以使用 dfs 与之前的陆地相连，并进行标记
                if not marked[i][j] and grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j, row_length, column_length, marked)
        return count

    def dfs(self, grid, i, j, m, n, marked):
        marked[i][j] = True

        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]

            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
                self.dfs(grid, new_i, new_j, m, n, marked)


if __name__ == '__main__':
    test_grid = [['1', '1', '1', '1', '0'],
                 ['1', '1', '0', '1', '0'],
                 ['1', '1', '0', '0', '0'],
                 ['0', '0', '0', '0', '0']]
    solution = Solution()
    result = solution.numIslands(test_grid)
    print(result)
