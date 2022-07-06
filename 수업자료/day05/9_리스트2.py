#  list는 index가 있기 때문에
# indexing, slicing이 가능

li = [10,20,30,40,50,60,70,80,90,100]
print("li[1]=",li[1])
print("li[1:5]=",li[1:5])       # slicing 옵션은 문자열과 똑같다

print("li[:7] =", li[:7])
print("li[7:] =", li[7:])

print("\nli[1]의 타입 :", type(li[1]))      # index의 타입은 요소의 타입이 되고 
print("li[1:2]의 타입 :", type(li[1:2]))    # slicing은 부분 리스트이기 때문에 타입이 list

print("\nli[:] =",li[:])
print("li[::2] =", li[::2])

print("li[::-1]=", li[::-1])

