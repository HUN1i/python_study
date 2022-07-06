# split()은 파이썬에서 한줄에 여러 데이터를 입력하는 형태로 자주 사용됨
name, age = input("이름 나이 : ").split()

print(f"{name} (= {age}세\n")

q = "두 정수를 입력 : "
n1, n2 = map(int, input(q).split())#꼭알아야함

print(f"n1 = {n1}, n2 = {n2}")
print("n1 + n2 =", n1 + n2)