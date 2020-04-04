"""
https://leetcode-cn.com/problems/trapping-rain-water/
https://leetcode-cn.com/problems/trapping-rain-water/solution/jie-yu-shui-by-leetcode/
https://leetcode-cn.com/problems/trapping-rain-water/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-8/
https://leetcode-cn.com/problems/trapping-rain-water/solution/xiong-mao-shua-ti-python3-shi-pin-jiang-jie-dan-di/
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)

        if length < 3:
            return 0

        res, idx = 0, 0
        stack = []

        while idx < length:
            while len(stack) > 0 and height[idx] > height[stack[-1]]:
                top = stack.pop()

                if len(stack) == 0:
                    break

                h = min(height[stack[-1]], height[idx]) - height[top]
                dist = idx - stack[-1] - 1
                res += (dist * h)

            stack.append(idx)
            idx += 1

        return res
