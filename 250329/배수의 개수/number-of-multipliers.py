numbers = []  

for _ in range(10):   
    num = int(input())  
    numbers.append(num)  

count_3 = 0  
count_5 = 0  

for num in numbers:
    if num % 3 == 0:
        count_3 += 1
    if num % 5 == 0:
        count_5 += 1

print(count_3, count_5) 
