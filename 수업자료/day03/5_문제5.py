cur = 2021

birth = int(input("생년월일 6자리 : "))
gender = int(input("주민등록번호 뒷자리 하나 :"))

year = birth // 10000

if gender == 1 or gender == 2 :
    year += 1900
elif gender == 3 or gender == 4 :
    year += 2000


age = cur - year + 1

print(f"성별정보가 {gender}이므로, {year}년생, {age}살 입니다")