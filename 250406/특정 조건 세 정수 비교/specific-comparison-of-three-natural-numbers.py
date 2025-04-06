a, b, c = map(int, input().split())

m=0
e=0

if a == min(a, b, c):
    m=1
else:
    m=0

if a == b == c:
    e=1
else:
    e=0

print(f"{m} {e}")
