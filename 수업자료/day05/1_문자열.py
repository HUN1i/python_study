# 문자열 : 단어나 문장을 표현하는 데이터 타입
# ' '나 " " 로 묶인 데이터

word = "Python"

print("word =", word, "\n")

# 1. 파이썬의 문자열은 +, * 연산이 가능하다
print(word + "hello")   # +는 이어붙이기

print(word* 3)         # *는 복사
# 2. 내장함수로 많은 기능이 구현되어 있다
word = word.upper()

print("word=", word)