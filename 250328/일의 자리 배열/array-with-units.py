a,b=map(int,input().split())
num=[a,b]


for i in range(8):
    num.append(num[-1]+num[-2])

for i in range(10):
    print(num[i]%10,end=' ')
