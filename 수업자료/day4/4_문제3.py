money = 1
total = 0

for day in range ( 1, 31) :
    total += money

    # 디버깅 코드
    #print(f"{day}일차) 예금 : {money:,}원, 저축 {total:,}원")
    money *= 2

print(f"한달 저축 금액 : {total:,}원")