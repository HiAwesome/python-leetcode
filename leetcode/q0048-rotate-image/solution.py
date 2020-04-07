"""
https://leetcode-cn.com/problems/rotate-image/
https://leetcode-cn.com/problems/rotate-image/solution/xuan-zhuan-tu-xiang-by-leetcode/
https://leetcode-cn.com/problems/rotate-matrix-lcci/
https://leetcode-cn.com/problems/rotate-matrix-lcci/solution/xuan-zhuan-ju-zhen-by-leetcode-solution/
"""


class Solution:

    def rotate(self, matrix):

        n = len(matrix[0])

        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        for i in range(n):
            matrix[i].reverse()
