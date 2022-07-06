# 리스트와 반복

for i in range(1,6) :
        print(i, end = "")
print()


# range()는 list로 변환해서 사용 가능
li = list(range(1,6))
print("\nli =", li)


# for문은 원래 리스트의 요소를 하나씩 대입하여 반복하는 방식
for n in [10,20,30,40,50] :
    print("n =",n)
print()

li = ["Python", "Java", "C++"]

for word in li :
    print("word =", word)