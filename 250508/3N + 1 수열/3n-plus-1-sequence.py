a=int(input())
i=0

while True:
    if a%2==0:
        a//=2
        i=i+1
    elif a%2==1:
        if a==1:
            break
        else:
            a*=3
            a+=1
            i+=1
print(i)
    

