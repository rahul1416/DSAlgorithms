'''
https://leetcode.com/problems/valid-palindrome/description/
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]