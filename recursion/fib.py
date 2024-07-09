'''
https://leetcode.com/problems/fibonacci-number/submissions/1314822565/
'''
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 :
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)