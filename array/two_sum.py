'''
https://leetcode.com/problems/two-sum/
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      num_dict = {}
      for i,num in enumerate(nums):
        compl = target - num
        if compl in num_dict:
          return [num_dict[compl],i]
        num_dict[num] = i
      return []