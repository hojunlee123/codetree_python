count_A = 0

for _ in range(3):
    symptom, temp = input().split()
    temp = float(temp)

    if symptom == 'Y' and temp >= 37:
        count_A += 1

if count_A >= 2:
    print("E")
else:
    print("N")
