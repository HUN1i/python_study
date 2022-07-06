# f-string 방식
# 문자열 내에서 바로 데이터를 채우는 방식

name = "홍길동"
age = 17
height = 168.2

print(f"이름 : {name} ({age}세, {height}cm)\n")

# 기능은 format 함수랑 똑같이 사용하면 된다
print(f"신장 : {height:.3f}cm")

money = 987654321
print(f"잔고 : {money:,}원")

word = "Python"
print(f"{word:$^30}")