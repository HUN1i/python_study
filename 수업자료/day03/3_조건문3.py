# elif : 위의 조건이 거짓이면 조건을 검사
# - 단독으로 사용 불가능
# - 참이면 종속문장을 수행

age = int(input("나이 입력 :" ))

if age >= 20 :
    print("성인", end = " ")

elif age >= 17 :
    print("고등학생", end = " ")

elif age >= 14 :
    print("중학생", end = " ")

else : 
    print("초등학생 이하", end = " ")

print("입니다")

# 범위가 삼각형 형태가 되어야 한다