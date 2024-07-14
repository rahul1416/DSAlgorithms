'''
https://leetcode.com/problems/maximum-subarray/description/
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ma = sum(nums)
        count = 0
        for i in range(0,len(nums)):
            count += nums[i]
            if count > ma:
                ma = count
            if count < 0:
                count = 0  
        return ma