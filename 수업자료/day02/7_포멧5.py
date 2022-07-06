# {}의 기능들

# 1. 소수점 제어
pi= 3.141592

print("pi = {}".format(pi))
print("pi = {:.2f}".format(pi))

# 2. 돈단위
money = 123456789

print("잔고 : {}원".format(money))
print("잔고 : {:,}원".format(money))

# 3. 출력 공간제어
word = "Python"

print("{}".format(word))
print("{:!<30}".format(word))
print("{:+>30}".format(word))
print("{:-^30}".format(word))

# 채울문자를 생략하면 공백이 채워진다
print("{:^30}".format(word))