n = 10
sum_val = 0
count = 0

for _ in range(n):
    num = int(input())
    if 0 <= num <= 200:
        sum_val += num
        count += 1

average = round(sum_val / count, 1)
print(sum_val, average)
