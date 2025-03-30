matrix = []  

for _ in range(3):
    row = list(map(int, input().split()))  
    matrix.append([x * 3 for x in row])  

for row in matrix:
    print(*row)  
