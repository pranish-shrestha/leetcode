'''
1. Two Sum
https://leetcode.com/problems/two-sum/
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}
        for index, value in enumerate(nums):
            if target-value in dict_:
                return [dict_[target-value], index]
            else:
                dict_[value] = index
