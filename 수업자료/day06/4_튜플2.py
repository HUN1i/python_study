# 튜플은 리스트처럼 순서(index)가 있다
# 즉, indexing 및 slicing 가능




tu = 90,10,20,40,30,50
# 초기화시 괄호가 없으면 tuple로 지정됨

print("tu의 타입 :", type(tu))
print("tu =",tu)

print("\ntu[2] =", tu[2])
print("tu[2]의 타입 :", type(tu[2]))

print("\ntu[2:5] =", tu[2:5])
print("tu[2:5]의 타입 :", type(tu[2:5]))

# 리스트를 슬라이싱->리스트
# 튜플을 슬라이싱->튜플

tu = 10,20,30

print("\ntu+(1,2,3) =", tu +(1,2,3))
#- 튜플과 리스트는 더할 수 없다

print("tu * 3 =",tu * 3)
