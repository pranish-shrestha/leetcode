'''
724. Find Pivot Index
https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1
'''


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum, right_sum = sum(nums), 0
        for i in range(len(nums)):
            right_sum += nums[i]
            if total_sum - right_sum == 0:
                return i
            total_sum -= nums[i]
        return -1
