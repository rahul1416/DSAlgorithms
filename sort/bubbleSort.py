arr = [15,16,6,8,5]
arr = [16,14,5,6,8]
def bubbleSort(arr):
    for i in range(0,len(arr)-1):
        flag = 0
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                a = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = a
                flag = 1
        if flag == 0:
            break
    return arr

print(bubbleSort(arr))
