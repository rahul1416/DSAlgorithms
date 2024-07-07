'''
https://leetcode.com/problems/reverse-integer/description/

Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
'''
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = x*-1
            num = int(str(x)[-1::-1])*-1
        else:
            num = int(str(x)[-1::-1])
        if num > 2**31-1 or num < -2**31:
            return 0
        
        return num

