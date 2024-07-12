'''
https://www.geeksforgeeks.org/problems/second-largest3735/1
'''
#User function Template for python3
class Solution:
    def print2largest(self, arr):
        # Code Here
        lar , sec = -1,-1
        for i in range(0,len(arr)):
            if lar < arr[i]:
                sec = lar
                lar = arr[i]
            elif lar!=arr[i]:
                sec = max(min(arr[i],lar),sec)
        return sec

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends