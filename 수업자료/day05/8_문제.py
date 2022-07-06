# 1. 국영수 점수를 한줄에 띄어쓰기로 한번에 입력받는다


#ex)
# 국 영 수 : 70 80 98
# 국 70, 영 80, 수 98
# 합계 : 248 (82.67)
q = "국 영 수 :"
국, 영, 수= map(int, input(q).split())
total = 국+영+수
avg = total/3
print(f"국어 : {국}, 영어 : {영}, 수학 : {수}")
print(f"합계 : {total} (={avg:.2f}\n" )

# 2. 사용자에게 ID, PW룰 입력받아서 아래의 계정과 같으면 로그인 성공을 출력
# 단, 대소문자에 상관없이 로그인 성공
ID = "itbank"
PW = "qwe@123"
userID = input("ID : ").lower()
userPW = input("PW : ").lower()

if ID == userID and PW == userPW :
    print(f"{ID}님 로그인을 환영합니다~")
else :
    print("일치하는 계정이 존재하지 않습니다")
