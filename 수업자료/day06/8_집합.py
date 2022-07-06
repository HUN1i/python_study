# 교집함, 합집합, 차집합

A = {1,2,3,4,5,6}
B = {4,5,6,7,8,9}

print(f"A=", A)
print(f"A=", A) 

# 1. 교집합 : 두 집합의 공통 부분

print("A & B =", A&B)
print("A & B =", A.intersection(B))

# 2. 합집합 : 두 집합의 전체
print("\nA | B =",A|B)
print("A | B =", A.union (B))

# 3. 차집합 : 두 집합의 차. 연산 순서에 영향을 받는다
print("\nA - B =", A - B)
print("B - A =", B - A)

print("\nA - B =", A.difference(B))
print("B - A =", B.difference (A))