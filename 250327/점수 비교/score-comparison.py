a,b=map(int,input().split())
i,j=map(int,input().split())

if(a>=i and i>j) or (a>i and i>=j) or (a>i and i>j):
    print('1')
else:
    print('0')
