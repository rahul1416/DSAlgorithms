'''
https://leetcode.com/problems/sort-colors/description/
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dict = {0:0,1:0,2:0}
        result = []
        for i in nums:
            dict[i] = dict[i] + 1
        ptr = 0
        for i in range(0,3):
            for _ in range(dict[i]):
                nums[ptr] = i
                ptr = ptr + 1

        return dict