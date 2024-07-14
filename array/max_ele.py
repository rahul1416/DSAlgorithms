'''
https://leetcode.com/problems/majority-element/submissions/1320824739/
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sol = None
        cnt = 0
        for i in nums:
            if cnt == 0:
                sol = i
            cnt += (1 if i == sol else -1)
        return sol

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = sorted(nums)
        return s[len(nums)//2]