n = int(input("정수 입력 : "))
count = 0
for i in range(1, n+1 ) :
    if n % i == 0 :
        print(i, end= " ")
        count += 1

print(f"(약수의 개수 = {count}개)")

if count == 2 :
    print("소수입니다")
else:
    print("소수가 아닙니다")