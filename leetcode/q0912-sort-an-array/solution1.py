"""
https://leetcode-cn.com/problems/sort-an-array/
https://leetcode-cn.com/problems/sort-an-array/solution/pai-xu-shu-zu-by-leetcode-solution/
"""
from typing import List


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        self.heap_sort(nums)
        return nums

    def heap_sort(self, nums):
        self.build_heap(nums)

        for i in range(len(nums) - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.max_heapify(nums, 0, i)

    def build_heap(self, heap):
        for i in range(len(heap) - 1, -1, -1):
            self.max_heapify(heap, i, len(heap))

    def max_heapify(self, heap, root, heap_length):
        p = root
        while p * 2 + 1 < heap_length:
            left, right = p * 2 + 1, p * 2 + 2

            if heap_length <= right or heap[right] < heap[left]:
                nex = left
            else:
                nex = right

            if heap[p] < heap[nex]:
                heap[p], heap[nex] = heap[nex], heap[p]
                p = nex
            else:
                break
