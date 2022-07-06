# input()은 모든 데이터를 읽기 위해서
# 기본적으로 문자열로 데이터를 가져온다

# 이때, 정수나 실수로 입력 받고 싶다면 앞서 배운 형변환을 활용한다

n1 = int(input("정수1 : "))
n2 = int(input("정수2 : "))

print(f"\nn1 = {n1}, n2 = {n2}")
print(f"n1 + n2 = {n1 + n2}")

r = float(input("\n반지름 : "))
pi = 3.141592

print(f"반지름 {r}의 원넓이 : {pi * r ** 2}cm")