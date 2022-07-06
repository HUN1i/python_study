#format : 형태, 서식
# formatting : 문자열에 형태만 잡아두고, 데이터를 한번에 채우는 방식

# 1. C언어 방식 (=옛날 방식)
name = "홍길동"
age = 22

print("이름 : %s, 나이 : %d세" % (name, age))

# 2. format() 함수 방식 (= 가장 보편적)
print("이름 : {}, 나이 : {}세" .format(name, age))

# 3. f-string 방식 (= 최신 방식, 가장 직관적)
print(f"이름 : {name}, 나이 : {age}세")
