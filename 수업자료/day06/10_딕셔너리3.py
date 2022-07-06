# key와 value는 자료형을 가리지 않는다

dt1 = {"one": 1, "two" :2, "three" :3}  # str : int
dt2 = {10:3.14, 20:"apple", 30:True}    # int : (float, str, bool)
dt3 = {(10,20):"apple",(20,30):"banana"}# tuple : str

print("dt1 =",dt1)
print("dt2 =",dt2)
print("dt3 =",dt3)

print("\ndt1['one] =", dt1['one'])
print("dt2[30] =", dt2[30])
print("dt3[(20,30)]=", dt3[(20,30)])

# key은 대체로 거의 str(문자열)이 사용된다
person = {"name":"홍길동",
    "age":22,
    "height":181.1,
    "hobby":["게임", "영화", "독서"]
    }

print("person의 이름 :", person['name'])
print("person의 나이 :", person['age'])
print("person의 신장 :", person["height"])
print("person의 취미 :", person["hobby"])

