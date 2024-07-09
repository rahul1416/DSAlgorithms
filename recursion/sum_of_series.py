'''
https://www.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1
'''

class Solution:
    def sumOfSeries(self,n):
        #code here
        if n == 0:
            return 0
        else:
            return n**3 + self.sumOfSeries((n-1)**3)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.sumOfSeries(N)) 
# } Driver Code Ends