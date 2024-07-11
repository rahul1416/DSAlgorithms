'''
https://www.geeksforgeeks.org/problems/insertion-sort/0
'''

class Solution:
    def insert(self, alist, index, n):
        j=index
        while j>0 and alist[j-1]>alist[j]:
            alist[j-1],alist[j]=alist[j],alist[j-1]
            j-=1
    def insertionSort(self, alist, n):
        for i in range(1,n):
            self.insert(alist,i,n)
        return alist

#{ 
 # Driver Code Starts

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
