'''
268. Missing Number
https://leetcode.com/problems/missing-number/
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_sum = len(nums)*(len(nums)+1)/2
        return int(max_sum - sum(nums))
