# replace : 문자열에서 지정한 부분을 교체하는 함수
word = "You need Java"

print("word =", word)

word = word.replace("Java", "Python")
print("word =", word)


# split : 문자열을 분한하는 함수, 결과가 list로 저장됨
result = word.split()

print("\nresult =", result)

# 변수를 나누어지는 개수와 맞게 두면 1:1로 저장됨
w1, w2, w3 = word.split()

print(f"w1 = {w1}, w2 = {w2}, w3 = {w3}")