

N = int(input())  # 정수 입력받기

for i in range(1, N + 1):  # 1부터 N까지 반복
    print(" ".join(f"{i}"*i))   # 숫자를 i번 반복하여 출력
