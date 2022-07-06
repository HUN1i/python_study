mart ={"다이제":1000, "메로나":500,"코카콜라":700,"츄파츕스":500}
menu = tuple(mart.keys())
print (menu)


values = list(mart.values())
print("가격 합계 :", sum(values))


for i in range(2) :
    m = input("메뉴 : ")
    v = int(input("가격 : "))

    mart[m] = v


print("\nmart =", mart)

