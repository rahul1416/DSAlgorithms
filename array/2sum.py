'''
https://leetcode.com/problems/two-sum/
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     a = target - nums[i]
        #     new_nums = nums[:]
        #     new_nums.pop(i)
        #     if a in new_nums:
        #         return [i, new_nums.index(a)+1]
        index_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in index_map:
                return (i,index_map[complement])
            index_map[num] = i