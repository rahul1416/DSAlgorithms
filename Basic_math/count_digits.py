'''
Given a number n. Count the number of digits in n which evenly divide n. Return an integer, total number of digits of n which divides n evenly.

Note :- Evenly divides means whether n is divisible by a digit i.e. leaves a remainder 0 when divided.
'''

class Solution:
    def evenlyDivides (self, N):
        # code here
        count = 0 
        original=N
        while N>0:
            d = N%10
            if d!=0 and original % d == 0:
                count+=1
            N//=10
        return count 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))