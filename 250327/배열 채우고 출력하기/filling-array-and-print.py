arr=list(map(str,input().split()))
arr1=[]


for i in range(len(arr)):
    arr1.append(arr[i])
arr1.reverse()

for i in range(len(arr1)):
    print(f"{arr1[i]}",end="")




