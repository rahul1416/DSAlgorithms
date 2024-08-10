from typing import List


class Solution:
    def convertToWave(self, n : int, arr : List[int]) -> None:
        # code here
        for i in range(0,n-1,2):
            arr[i], arr[i+1] = arr[i+1], arr[i]

        return arr
