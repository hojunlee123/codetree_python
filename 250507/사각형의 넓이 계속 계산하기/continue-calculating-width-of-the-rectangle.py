while True:
    line = input().strip()
    width, height, ch = line.split()
    area = int(width) * int(height)
    print(area)
    if ch == 'C':
        break

        
