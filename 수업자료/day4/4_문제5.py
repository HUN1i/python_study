n1 = int(input("정수1 :"))
n2 = int(input("정수2 :"))

big = n1 if n1 > n2 else n2
maximum = 0
for i in range(1, big + 1):
    if n1 % i == 0 and n2 % i == 0 :
        print(i, end = " ")
    maximum = i
print("\n최대공약수 = ", maximum)