"""
https://leetcode-cn.com/problems/sort-an-array/
https://leetcode-cn.com/problems/sort-an-array/solution/pai-xu-shu-zu-by-leetcode-solution/
"""
from random import random
from typing import List


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums

    def randomized_quicksort(self, nums, left, right):
        if right - left <= 0:
            return

        mid = self.randomized_partition(nums, left, right)
        self.randomized_quicksort(nums, left, mid - 1)
        self.randomized_quicksort(nums, mid + 1, right)

    def randomized_partition(self, nums, left, right):
        pivot = random.randint(left, right)
        # change position
        nums[pivot], nums[right] = nums[right], nums[pivot]
        i = left - 1
        for j in range(left, right):
            if nums[j] < nums[right]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i
