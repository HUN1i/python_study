# for 문을 활용하여 푼다

# 1. 구구단 2단을 출력 ( 단, x9까지만)
dan = 2

for i in range(1 , 10) :
    print (f"{2} x {i} = {2 * 1}")


# 2. 입력 받은 구구단 출력
dan = int(input("몇 단? "))

for i in range ( 1, 10):
    print(f"{dan} x {i} = {dan * i}")

# 3. 역순 출력