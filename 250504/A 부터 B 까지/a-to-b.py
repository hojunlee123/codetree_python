A, B = map(int, input().split())

current = A
while current <= B:
    print(current, end=" ")
    if current % 2 == 0:
        current += 3  
    else:
        current *= 2  
