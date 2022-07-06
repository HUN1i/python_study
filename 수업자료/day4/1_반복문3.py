# 반복의 형태
# 1. 지정 횟수 반복 : 횟수가 있는 반복. ex) 10번, 50번 등
# 2. 불특정 횟수 반복 : 횟수가 마땅히 없는 반복. ex) 종료할 때까지

n = 1

while n != 0 :
    n = int(input("정수 입력(0 = 종료)"))

    print(f"n = {n}\n")
print()


# 무한반복을 활용
# 무한반복은 종료하기 위해서 보조 제어문의 도움이 필요하다
while True :
    n = int(input("정수 입력(0 : 종료)"))

    if n == 0 :
        break # break : 반복을 '즉시' 탈출

    print(f"n = {n}\n")