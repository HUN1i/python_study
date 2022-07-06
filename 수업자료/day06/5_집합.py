# set : 집합
# - 순서x, 중복x, 수정x, 삭제o

li = [10,10,10,20,20,30]
st = (10,10,10,20,20,30)

print("li =", li)
print("st =", st)   # 중복이 없다

print("\nli[0] =", li[0])
#print("st[0] =",st[0])  # 순서(=index)가 없다

# 즉, index가 없기 때문에
# indexing과 slicing이 불가능

# list, tuple <-> set 간에는 형변환이 성립한다
li = [1,1,1,1,1,2,2,2,2,3,3,4,4,4,5,5]

li = set(li)
print("li =",li)

li = list(li)
print("li =",li)

# 한번에 하는 법
li = [10,10,10,20]

li = list(set(li))
print("li =",li)

