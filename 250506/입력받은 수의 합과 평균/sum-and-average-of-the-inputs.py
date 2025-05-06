n = int(input())
sum_val = 0

for _ in range(n):
    num = int(input())
    sum_val += num

avg = round(sum_val / n, 1)
print(sum_val, avg)
