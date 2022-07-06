# 딕셔너리 : key와 value의 한쌍의 데이터

dt = {"name":"홍길동", "age":22, "height":170.8}
#       key : value

li = ["홍길동", 22, 170.8]
#        0      1     2

print("li[0] =", li[0])     # list는 데이터에 접근하기 위해서 index를 사용
print(dt['name'])
# dict는 데이터(value)에 접근하기 위해서 key를 사용
# 즉, 사용자가 직접 정의한 index라고 생각하면 좋다.

print("dt['height'] =",dt['height'])
# print("dt['address']=", dt['address'])
# - 없는 key으로 참조하면 에러

print("dt의 타입 :", type(dt))
