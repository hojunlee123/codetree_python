score = int(input())  

for s in range(score, 101):  
    if s >= 90:
        grade = "A"
    elif s >= 80:
        grade = "B"
    elif s >= 70:
        grade = "C"
    elif s >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print(f"{grade}",end=' ')

