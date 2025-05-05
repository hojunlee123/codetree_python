n = int(input())

classroom_cleaning = 0
hallway_cleaning = 0
bathroom_cleaning = 0

for day in range(1, n + 1):
    if day % 12 == 0:
        bathroom_cleaning += 1
    elif day % 2 == 0:
        classroom_cleaning += 1
    elif day % 3 == 0:
        hallway_cleaning += 1

print(classroom_cleaning, hallway_cleaning, bathroom_cleaning)
