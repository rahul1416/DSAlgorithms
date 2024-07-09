'''
https://www.geeksforgeeks.org/problems/find-all-factorial-numbers-less-than-or-equal-to-n3548/1
'''

class Solution:
    def factorialNumbers(self, n):
        arr=[]
        def helper(fac_of,nxt):
            if fac_of<=n:
                arr.append(fac_of)
                helper(fac_of*(nxt+1),nxt+1)
                
        helper(1,1)
        return arr
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends