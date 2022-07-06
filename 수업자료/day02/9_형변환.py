# 형변환(=casting) : 데이터 타입. 즉, 자료형을 변환하는 것

n1 = "10"
n2 = "20"

print(f"n1 + n2 = {n1 + n2}")
print(f"n1의 타입 : {type(n1)}")
print(f"n2의 타입 : {type(n2)}\n")

n1 = float(n1) # 자료형(데이터) 형식으로 변환 가능
n2 = float(n2)

print(f"n1 + n2 = {n1 + n2}")
print(f"n1의 타입 : {type(n1)}")
print(f"n2의 타입 : {type(n2)}\n")
n1 = int(n1) 
n2 = int(n2)

print(f"n1 + n2 = {n1 + n2}")
print(f"n1의 타입 : {type(n1)}")
print(f"n2의 타입 : {type(n2)}\n")
