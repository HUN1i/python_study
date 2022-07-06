
from os import stat


station = int(input("몇 정거장?"))

if station < 10 :
    total = station * 2

else :
    total = stat * 4

if total >= 60 :
    hour = total // 60
    miniute = total % 60

    print (f"총 소요시간은 {hour}시간 {miniute}분 입니다~")
else :
    print (f"총 소요시간은 {total}분 입니다~")










