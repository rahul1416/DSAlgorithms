'''
https://www.geeksforgeeks.org/problems/prime-number2314/1
'''

from math import sqrt

class Solution:
    def isPrime (self, N):
        # code here
        if N == 1 :
            return 0
        else: 
            for i in range(2,int(sqrt(N))+1):
                if N%i == 0:
                    return 0
            return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends