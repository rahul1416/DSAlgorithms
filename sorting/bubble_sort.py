'''
https://www.geeksforgeeks.org/problems/bubble-sort/1
'''
class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
        for i in range(0,n):
            for j in range(0,n):
                if arr[i]<arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr, n)
        for i in arr:
            print(i,end=' ')
        print()
