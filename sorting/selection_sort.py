'''
https://www.geeksforgeeks.org/problems/selection-sort/1
'''
class Solution: 
    def select(self, arr, i):
        min_index=i
        for j in range (i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        return min_index    
     
        # code here 
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            min_index=self.select(arr,i)
            arr[i],arr[min_index]=arr[min_index],arr[i]
            
        return arr    
