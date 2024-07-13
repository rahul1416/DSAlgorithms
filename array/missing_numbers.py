'''
https://leetcode.com/problems/missing-number/description/
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = len(nums)
        total = ((s)*(s+1))/2
        count = 0
        for num in nums:
            count+=num
        return int(total-count)