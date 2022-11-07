"""
https://leetcode.com/problems/missing-number/
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        n = len(nums)
        actual_sum = (n*(n+1))/2
        return int(actual_sum-nums_sum)
        