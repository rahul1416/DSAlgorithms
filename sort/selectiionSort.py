a = [7,4,10,8,3,1]
n = 6
for i in range(0,n-1):
    mini = i
    for j in range(i,n):
        if a[mini] > a[j]:
            mini = j
        # print(a)
    if mini != i:
        s = a[mini]
        a[mini] = a[i]
        a[i] = s
        # print(a)
print(a)