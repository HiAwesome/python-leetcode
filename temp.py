from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        j = 0

        for index in range(len(nums)):
            if val != nums[index]:
                nums[j] = nums[index]
                j += 1

        return j


if __name__ == '__main__':
    s1 = Solution()
    print(s1.removeElement([3, 2, 2, 3], 3))
