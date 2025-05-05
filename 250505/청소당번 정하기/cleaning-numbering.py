n = int(input())

classroom = 0  
hallway = 0   
bathroom = 0   

for day in range(1, n + 1):
    if day % 12 == 0:
        bathroom += 1
    elif day % 3 == 0:
        hallway += 1
    elif day % 2 == 0:
        classroom += 1

print(classroom, hallway, bathroom)
