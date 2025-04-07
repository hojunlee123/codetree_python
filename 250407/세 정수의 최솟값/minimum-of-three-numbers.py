a, b, c = map(int, input().split())

min_val = a if a < b and a < c else (b if b < c else c)
print(min_val)
