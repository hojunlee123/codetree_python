A, B = map(int, input().split())

start = min(A, B)
end = max(A, B)

total = 0
for i in range(start, end + 1):
    if i % 5 == 0:
        total += i

print(total)
