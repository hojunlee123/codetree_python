N = int(input())
product = 1

for i in range(1, 11):  
    product *= i
    if product >= N:
        print(i)
        break
