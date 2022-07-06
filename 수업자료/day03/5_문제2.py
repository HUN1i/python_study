A = 5
B = 7

cur = int(input("몇 층? "))

disA = cur - A
disB = cur - B

if disA < 0 :
    disA *= -1
if disB < 0 :
    disB *= -1
print(f"차이) A : {disA}, B : {disB}")

if disA < disB :
    print("A를 호출합니다~")
else :
    print("B를 호출합니다~")