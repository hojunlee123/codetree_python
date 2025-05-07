N = int(input())
count = 0
i = 1

while N > 1:
    N = N // i
    count += 1
    i += 1

print(count)
