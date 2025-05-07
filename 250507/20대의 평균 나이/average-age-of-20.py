count = 0
total = 0

while True:
    age = int(input())
    if 20 <= age <= 29:
        total += age
        count += 1
    else:
        break

average = total / count
print(f"{average:.2f}")
