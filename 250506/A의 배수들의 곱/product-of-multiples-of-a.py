A, B = map(int, input().split())

product = 1
found = False 

for i in range(1, B + 1):
    if i % A == 0:
        product *= i
        found = True

print(product if found else 1)
