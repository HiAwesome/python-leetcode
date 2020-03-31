"""
https://leetcode-cn.com/problems/two-sum/
https://leetcode-cn.com/problems/two-sum/solution/liang-shu-zhi-he-by-leetcode-2/
https://leetcode-cn.com/problems/two-sum/solution/xiao-bai-pythonji-chong-jie-fa-by-lao-la-rou-yue-j/
"""
from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, num in enumerate(nums):
            if dic.get(target - num) is not None:
                return [i, dic.get(target - num)]
            # 这句不能放在 if 语句之前，否则 target-num=num 时返回了 [0,0]
            dic[num] = i
