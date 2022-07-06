# 조건 연산자
# - 조건에 따라서 값을 '선택'하는 연산자

# 형태)
# 참 if 조건식 else 거짓
n = int(input("정수 입력 : "))

result = "짝수" if n % 2 == 0 else "홀수"

print(f"{n}(은)는 {result} 입니다~")
