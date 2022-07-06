# while : 조건으로 반복하는 구문
# for : 범위로 반복하는 구문

for i in range(5) : # range (n) : 0 ~ (n-1) 의 범위를 생성
    print(f"i = {i}")

print()

for i in range (1 , 6): # range(start , end) : start ~ (end - 1)의 범위를 생성
    print(f"i = {i}")

    print()

for i in range(1, 11, 2) : # range (a, b, c) : a~ (b - 1) 까지 c씩 증가하는 범위 생성
    print(f"i = {i}")

print()

# 마지막 step 옵션은 2칸 , 3칸씩 쓰기보단 '역으로 반복'하기 위해 사용

for i in range(5,0, 1) : # 5~(0 + 1) 까지의 범위를 생성
    print(f"i = {i}")
