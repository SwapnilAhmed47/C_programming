# YouTube Version:
arr = [6, 3, 8, 2, 4]
counter = 1
while counter<len(arr):
    for i in range(len(arr) - counter):
        if arr[i]>arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
    
    counter+=1
print("")
print("YouTube Version:",arr)
print("")


# Understandable Version:
numbers = [17, 3, 9, 21, 2]
for i in range(len(numbers)-1):
    for j in range(len(numbers)-i-1):
        print(j)
        if numbers[j] > numbers[j+1]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp
print("Versity Version:",numbers)
