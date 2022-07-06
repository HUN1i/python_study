# 내장함수
dt = {"Python" : 90, "C++":70, "Java":80, "C언어" :85}

# get() : 지정한 key의 value값을 반환
print("dt['Python'] =",dt['Python'] )
print("dt.get('Python') =",dt.get('Python') )

# print("dt[SQL]=", dt('SQL'))
print("dt.get(SQL)=", dt.get('SQL'))
# []는 없는 key인 경우 에러
# get()은 없는 key인 경우 None 을 반환


# key(): 딕셔너리에서 key값만 싹 뽑아낸다
# - list나 다른 묶음타입으로 형변환해서 쓰자
k = list(dt.keys())

print("\nk =", k)
print("k[1] =",k[1])

# values() : 딕셔너리에서 value값만 싹 뽑아낸다
# - 마찬가지로 형변환해서 사용
v= list(dt.values())

print("\nv =", v)
print("v[2] =", v[2])

# items() : 딕셔너리에서 (key, value) 형태의 튜플로 뽑아낸다
# - 형변환
it = list(dt.items())

print("\nit =", it)
print("it[0] =", it[0])
print("it[0][1] =", it[0][1])