'''
https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1
'''

class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        # greater = max(A, B)
        # smallest = min(A, B)
        # for i in range(greater, A*B+1, greater):
        #     if i % smallest == 0:
        #         return i, (A*B)//i
        gcd = self.findgcd(A, B)
        lcm = A * B // gcd
        return lcm, gcd

    def findgcd(self, A, B):
        while B != 0:
            temp = B
            B = A % B
            A = temp
        return A


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends