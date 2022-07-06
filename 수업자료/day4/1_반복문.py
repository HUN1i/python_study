# 반복문 : 코드의 흐름을 루프

# while : 조건식이 참이면 종속문장을 수행. 종속문장이 끝나면 다시 조건으로 이동

i = 1

while i <= 20 :
    print(f"{i} : Hello World!!!")
    i +=2

print(f"반복 후 i = {i}\n")

# 5~ 1 : Hello World

i = 5
while i >= 1 :
    print(f"{i} : Hello World!!")
    i -= 1

print(f"반복 후 i = {i}")
    