items = {
    "book": 3000,
    "mask": 1000,
    "pen": 500
}

N = int(input())  

affordable = [name for name, price in items.items() if price <= N]

if affordable:
    most_expensive = max(affordable, key=lambda name: items[name])
    print(most_expensive)
else:
    print("no")
