# format() 함수 방식
# - 문자열의 내장 함수 중 하나
# - 따라서, 문자열.format() 형태로 사용된다
# - 서식문자는 {}만 사용한다

name = "홍길동"
age = 31
height = 175.3

print("이름 : {} ({}세, {})cm)\n" .format(name, age, height))
# 마찬가지로 순서대로 채워진다
# 소수점은 무한대가 아니라면 딱 저장된 만큼만 출력된다

result = "이름 : {} ({}세)"

print(result.format(name, age))

result = "이름 : {} ({}세)".format(name, age)

print(result)