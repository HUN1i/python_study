# 튜플: 리스트처럼 데이터를 묶어서 저장가능. 단, 요소의 변경이 불가능

# list : 순서o,중복o, 수정o
# tuple : 순서o,중복o, 수정x

li = [10,20,30,10,20]
tu = (10,20,30,10,20)# 튜플은 () 사용

print(f"li = {li}, tu = {tu}")

li[1] = 25
#tu[1] = 25 # tu은 요소의 변경이 불가능
print(f"li = {li}, tu = {tu}")

# list와 tuple간에는 형변환이 성립한다
print("tu의 타입 :", type(tu))

tu = list(tu)
print("tu =", tu)
tu[2] = 33
print("tu =", tu)

tu = tuple(tu)
print("tu =", tu)