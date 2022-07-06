# 보조 제어문 : 제어문을 보조하는 구문

# 1. pass : 그냥 다음 코드로 넘어감
# - 주로 , 빈 종속문장을 채우는 용도로 사용됨

if True :
    pass #<-비우면 에러나기 때문에 사용


# 2. break : 제어문을 즉시 탈출

for i in range(1, 11) :
    if i == 5 :
        break
    
    print(i, end = " ")

print()

# 3. continue : 제어문을 즉시 처음으로 돌림
for i in range(1,11):
    if i == 5 :
        continue

    print(i, end = " ")