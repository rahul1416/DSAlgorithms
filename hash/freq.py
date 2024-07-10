class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # code here
        arr2 = []
        for i in range(0,N):
            count = 0
            for j in range(0,N):
                if i+1 == arr[j]:
                    count+=1
            # print(count,end=' ')
            arr2.append(count)
        for i in range (N):
            arr[i] = arr2[i]
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__=="__main__":
	T=int(input())
	while(T>0):
		N=int(input())
		arr=[int(x) for x in input().strip().split()]
		P=int(input())
		ob=Solution()
		ob.frequencyCount(arr, N, P)
		for i in arr:
			print(i, end=" ")
		print()
		T-=1



# } Driver Code Ends