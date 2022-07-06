# C언어 방식
# %라고 하는 포멧(= 서식) 문자를 사용하는 방식

# %s : string, 문자열이 들어갈 자리
# %d : decimal, 10진 정수 자리
# %f : float, 실수가 들어갈 자리

# 아래는 안외워도 좋다
# %o : octal, 8진 정수 자리
# %x : hexa, 16진 정수 자리

name = "홍길동"
age = 25
height = 169.123456

print("이름 : %s (%d세, %fcm)" % (name, age, height))
# 서식 문자에는 뒤의 데이터가 순서대로 채워진다!!!

print("\n이름은 %s 입니다~" %name)
# 데이터를 하나만 채울경우 ()를 생략 가능
# 둘 이상은 무조건 () 필요

# %f는 기본적으로 실수를 소수점 6자리를 기본으로 출력한다
# 제어를 위해선, %.nf로 제어가능 (단, n은 자연수)

print("\n이름 : %s (%d세, %.2fcm)\n" % (name, age, height))


# 포멧은 바로 출력할 필요없이 변수로 저장 받을 수도 있다
result = "이름 : %s (%d세)"

print(result % (name, age))

# 바로 완성 후 저장도 가능
result = "이름 : %s (%d세)" % (name, age)

print(result)