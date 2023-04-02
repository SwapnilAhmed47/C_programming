n=int(input(""))
l1=[]
for i in range(n):
    var=input().split(" ")
    count=0
    for j in var:
        count+=int(j)
    l1.append(count)
l1.sort()
print(l1)