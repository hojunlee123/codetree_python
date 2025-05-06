A, B = map(int, input().split())
sum_val = 0

start = min(A, B)
end = max(A, B)

for i in range(start, end + 1):
    if i % 6 == 0 and i % 8 != 0:
        sum_val += i

print(sum_val)
