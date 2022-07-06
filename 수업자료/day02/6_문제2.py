#pdf 11p
birth = "2006년 3월 28일"
age = "16"
kor = 96
eng = 97
mat = 68

print(f"생년월일:{birth}")
print(f"저는 {age}살 입니다.^^")
print(f"국어 {kor}점, 영어 {eng}점, 수학 {mat}점")
print(f"합계: {kor+eng+mat}")
print(f"평균: {(kor+eng+mat)/3}")


print(f"""
생년월일 : {birth}
저는 {age}살 입니다. ^^
국어 {kor}점, 영어 {eng}점, 수학 {mat}점
합계: {kor+eng+mat}
평균: {(kor+eng+mat)/3:.2f}""")

# {변수명:기능}
# 기능에 .2f는 소수점 2자리까지 제어