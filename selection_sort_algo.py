num = [5, 3, 8, 6, 7, 2]
for i in range(len(num)-1):
    for j in range(i+1, len(num)):
        if num[j]<num[i]:
        #   num[i], num[j] = num[j], num[i]   -----> This is advance way in python
            temp = num[j]
            num[j] = num[i]
            num[i] = temp
        print(num)
