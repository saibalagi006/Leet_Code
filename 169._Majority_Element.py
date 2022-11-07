"""
https://leetcode.com/problems/majority-element/
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}
        for idx,num in enumerate(nums):
            if(num not in dict1.keys()):
                dict1[num] = 1
            else:
                dict1[num]+=1
        max1 = 0
        for key,val in dict1.items():
            if(val>max1):
                max1 = val
                key_max = key
        return key_max
                