class Solution:
    def pairWithMaxSum(self, arr, N):
        # Your code goes here
    
        n = len(arr)
        maxi = float('-inf') 
        summ = 0
        
        for i in range(n-1):
            summ = arr[i] + arr[i+1]
            if summ > maxi:
                maxi = summ
    
        return maxi

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.pairWithMaxSum(a, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends