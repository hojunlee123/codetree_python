A, B = map(int, input().split())
product = 1

for i in range(A, B + 1):
    product *= i

print(product)
