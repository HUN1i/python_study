# 함수(function) : 일정길이의 코드를 이름으로 묶어둔 것
# - 즉, 특정 기능을 구현해 놓은 것

# 내장함수 : 특정 타입에 이미 구현되어 있는 함수를 의미
# 즉, 문자열 내장함수란, 문자열에 이미 구현되어 있는 기능을 의미한다
# count() : 지정한 문자열 개수 반환

word = "Welcome to Python World"

n = word.count("o")
print("o의 개수 :", n)

n = word.count("python")
print("python의 개수 :", n, "\n")

# find() : 지정한 문자열에 몇번째 index가 있는지 반환
i = word.find("p")

print("P의 index :", i)
print("word[11] =", word[11])
i = word.find("p", 12)
print("다음 P의 index :", i)

i = word.find("World")
print("World의 위치 :", i)
print("word[18:18 + 5] =", word[18:18 + 5])

i = word.find("java")       # 없는 문자열은 -1 반환됨
print("\njava의 위치 :", i)

# index() : find()랑 똑같은 함수. 단, 없는 문자열을 찾으면 에러
i = word.index("java")
print("java의 위치 :", i)