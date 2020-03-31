"""
https://leetcode-cn.com/problems/sort-an-array/
https://leetcode-cn.com/problems/sort-an-array/solution/pai-xu-shu-zu-by-leetcode-solution/
"""
from typing import List


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums

    def merge_sort(self, nums, left, right):
        if left == right:
            return

        mid = (left + right) // 2
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)

        tmp = []
        i, j = left, mid + 1

        while i <= mid or j <= right:
            if i > mid or (j <= right and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1

        nums[left: right + 1] = tmp
