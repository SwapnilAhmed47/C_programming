arr = [5, 5, 1, 2, 2, 2, 2, 3, 4, 7 ,8 ,8]
li = []
for i in arr:
    if i not in li:
        li.append(i)
for i in range(len(li)):
    count=0
    for j in range(len(arr)):
        if li[i]==arr[j]:
            count+=1
    print(f"{li[i]} - {count} times")