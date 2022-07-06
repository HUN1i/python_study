word = "메뉴"
price = 1000

menu = f"""{word:=^28}
새우 만두 1개 : {price}원
10개 이상 구매시 : 15% 할인
100개 이상 구매시 : 25% 할인
현금결재 시 결제금액의 10% 할인
>>>"""

count = int(input(menu))

total = price * count

if count >= 100 :
    total *= 0.75
elif count >= 10 :
    total *= 0.85

total = int(total)
cash = int(total * 0.9)

print(f"가격 : {total:,}원, 현금가 : {cash:,}원")