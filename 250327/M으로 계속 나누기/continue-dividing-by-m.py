N, M = map(int, input().split())

# Please write your code here.
print(f"{N}")
while N>=M:
    N=N//M
    print(f"{N}")
    