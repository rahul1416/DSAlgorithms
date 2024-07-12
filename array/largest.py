'''
https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0
'''

from typing import List
class Solution:
    def largest(self, n : int, arr : List[int]) -> int:
        # code here
        lar = arr[0]
        for i in range(n):
            if arr[i] > lar:
                lar = arr[i]
        return lar


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.largest(n, arr)

        print(res)

# } Driver Code Ends