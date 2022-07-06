#비교 연산자 : 데이터의 대소관계를 비교
# - 결과가 bool 타입(참/거짓)
# - 종류 : >, <, >=, <=, ==, !=

print(True)  # 참
print(False) # 거짓

print(type(True))
print(type("True"))
print()

n = 10

print(f"(n) > 5 결과 : {n > 5}")
print(f"{n} < 5 결과 : {n<5}")
print(f"{n} > 10 결과 : {n>=10}")
print(f"{n} >= 10 결과 : {n >= 10}")

print (f"{n} == 10 결과 : {n == 10}")   # 같으면 참, 다르면 거짓
print (f"{n} != 10 결과 : {n != 10 }")  #같으면 거짓, 다르면 참

# 비교의 결과고 변수에 저장할 수 있다
result = n == 11
#        = false
print ("\nresult =" , result)