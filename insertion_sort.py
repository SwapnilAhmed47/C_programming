arr = [17, 3, 9, 21, 2]
for i in range(1, len(arr)):
    current = arr[i]
    j = i - 1
    while (arr[j]>current and j>=0):
        arr[j+1] = arr[j]
        j-=1
    arr[j+1]=current
print(arr)
