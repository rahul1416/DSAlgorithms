'''
https://leetcode.com/problems/single-number/
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = {}
        for i in range(0,len(nums)):
            if nums[i] in s.keys():
                s[nums[i]] += 1
            else:
                s[nums[i]] = 1
        value = list(filter(lambda x: s[x] == 1, s))[0]
        return value