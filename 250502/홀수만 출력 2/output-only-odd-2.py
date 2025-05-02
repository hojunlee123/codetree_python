b,a=map(int,input().split())

for i in range(0,b-a+1):
    c=b-i
    if(c%2==1):
        print(c,end=' ')