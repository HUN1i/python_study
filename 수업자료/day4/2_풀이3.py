# 4-1: 단순한 출력
n = int(input("정수 입력 : "))

while n != 0 : 
    print(n % 10, end = "")

    n //= 10

print()

# 4-2. 정수로 저장 받기
n = int(input("\n다시 입력"))
while n != 0 :  
    rev = rev * 10 + n % 10

    n //= 10

print("거꾸로 수 :" , rev)
print ( "거꾸로 수 + 123 :", rev + 123)
# 1회차)
# n = 123, rev = 0
# rev = 0 * 10 + 123 % 10
# = 0 + 3
#2회차)
# n = 12, rev = 3
#rev = 3 * 10 + 12 % 10
# 30 + 2
#3회차)
#n = 1, rev = 32

# rev = 32 * 10 + 1 % 10
# = 320 + 1
