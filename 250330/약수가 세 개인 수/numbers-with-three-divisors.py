start, end = map(int, input().split())  
count = 0  

for num in range(start, end + 1):  
    divisors = [i for i in range(1, num + 1) if num % i == 0]  
    if len(divisors) == 3:  
        count += 1

print(count)  

