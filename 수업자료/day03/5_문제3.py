kor =int(input("국어 성적을 입력하시오 :"))
mat =int(input("수학 성적을 입력하시오 :"))
eng =int(input("영어 성적을 입력하시오 :"))
값= (kor+mat+eng)/3
avg = total/3
if kor and eng and mat>100:
    print("오류")


if avg >= 0 and avg <= 100 :
    if avg >=90 :
        rank ="A"
    elif avg>=80:
        rank ="B"
    elif avg>=70:
        rank ="C"
    elif avg>=60:
        rank ="D"
    else :
        rank = "F"
else :
    print("부적합한 점수입니다!")
print (f"{rank}등급 입니다~")