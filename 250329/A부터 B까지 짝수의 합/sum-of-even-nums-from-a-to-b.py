A, B = map(int, input().split())  
even_sum = 0  
for i in range(A, B + 1):  
    if i % 2 == 0:  
        even_sum += i 

print(even_sum)  
