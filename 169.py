'''
169. Majority Element
https://leetcode.com/problems/majority-element/
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element, majority_element_count = 0, 0
        nums_set = set(nums)

        for num in nums_set:
            if nums.count(num) > majority_element_count:
                majority_element = num
                majority_element_count = nums.count(num)

        return majority_element
