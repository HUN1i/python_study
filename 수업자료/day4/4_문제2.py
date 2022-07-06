word = "자판기"
cola = 1200
cider  = 1200
georgia = 1000
confidence = 600
import os

money = int(input("돈을 투입하세요 : "))
menu = f"""{word:=^26}
    콜라    :{cola:,}원
    사이다  :{cider:,}원
    조지아  :{georgia:,}원
    컨피던스:{confidence:,}원
    >종료

음료를 선택하세요 : """

#while true는 반복문

while True : 
    juice = input(menu)
    if juice == "콜라":
        select = cola
    elif juice == "사이다":
        select == cider
    elif juice == "조지아" :
        select == georgia
    elif juice == "컨피던스" :
        select == confidence
    elif juice == "종료":
        print("프로그램을 종료합니다")
        break
    else :
        select = 0
    if money >= select:
        money -= select
    else :
        print("잔액이 부족합니다!!!")


    print(f"잔액 : {money:,}원")

    
    os.system("pause")
    os.system("cls")