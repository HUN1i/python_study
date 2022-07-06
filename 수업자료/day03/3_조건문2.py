# else : 위의 조건이 거짓이면 자동으로 실행되는 구문
# - 단독으로 사용 불가능

age = int(input("나이 입력 :"))

if age >= 20 :
    print("성인", end = " ")
# 사이엔 아무것도 쓰면 안됨
else :
    print("미성년자", end = " ")

print("입니다~")
