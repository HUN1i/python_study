li = [70,10,20,50,80,30]

# append() : 가장 뒤에 데이터를 추가

li.append(40)
print("li =", li)

# insert() : 지정한 index에 데이터를 추가
li.insert(2,15)
print("li =", li)

# pop() : 지정한 index의 데이터를 꺼낸다

n = li.pop(4)
print("li =", li)
print("꺼낸 값 :", n)

# extend() : 요소를 한번에 추가
li.extend([100,200,300])
print("\nli =", li)

# index() : 지정한 요소가 어디에(index)있는지 반환
i = li.index(40)
print("40의 index =", i)
print("li[6] =",li[6])

print("다음 40의 index =", i)
print("li[10] =", li[10])

# count() : 지정한 요소가 몇개인지 반환
n = li.count(40)
print("\n40의 개수 :",n)

# reverse() : 리스트를 거꾸로 뒤집는다
li.reverse()
print("li =", li)

# sort() : 리스트를 정렬
li.sort("\n;li =", i)
li.sort(reverse)
