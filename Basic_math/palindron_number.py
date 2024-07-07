'''
https://leetcode.com/problems/palindrome-number/description/
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        z = y [::-1]
        if y == z:
            return True
        else:
            return False