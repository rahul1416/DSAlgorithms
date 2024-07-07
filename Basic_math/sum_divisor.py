'''
https://www.geeksforgeeks.org/problems/sum-of-all-divisors-from-1-to-n4738/1
'''

class Solution:
    def sumOfDivisors(self, N):
    	#code here 
        count = 0 
        for i in range(1,N+1):
            count += i*(N//i)
        return count
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
# } Driver Code Ends