N, M = map(int, input().split())

grid1 = [list(map(int, input().split())) for _ in range(N)]
grid2 = [list(map(int, input().split())) for _ in range(N)]

result = []
for i in range(N):
    row = []
    for j in range(M):
        if grid1[i][j] == grid2[i][j]:
            row.append(0)
        else:
            row.append(1)
    result.append(row)

for row in result:
    print(*row)
