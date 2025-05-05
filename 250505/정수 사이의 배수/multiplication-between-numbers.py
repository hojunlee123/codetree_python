A, B = map(int, input().split())

total = 0
count = 0

for i in range(A, B + 1):
    if i % 5 == 0 or i % 7 == 0:
        total += i
        count += 1

average = total / count if count != 0 else 0

print(f"{total} {round(average, 1)}")
