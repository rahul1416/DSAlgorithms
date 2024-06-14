a = [5,4,10,1,6,2]
n = 6
def insertionSort(a,n):
    for i in range(1,n):
        temp = a[i]
        j = i-1
        while (j>=0 and a[j]>temp):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = temp
        # print(a)
    return a
print(insertionSort(a,n))