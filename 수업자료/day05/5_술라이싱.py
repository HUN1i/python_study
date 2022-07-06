# indexing : index가지고 데이터 하나를 참조
# slicing : index를 범위로 처리해서 참조

word = "Welcome to Python!"
#       012345678901234567
# indexing
print("word[1] = ", word[1])
#slicing
print("word[1:5] =", word[1:5])     # [start : end - 1]

print("word[:9] =", word[:9])       # start를 생략하면 0번부터
print("word[3:] =", word[3:])       # end 생략하면 끝까지

print("word[:] =", word[:])         # 둘다 생략시 처음부터 끝까지

print("word[::2] =", word[::2])     #[start : end - 1 : step]
print("word[1::2] =", word[1::2])

# step는 2칸씩 뛰는 옵션보다 역순으로 더 자주 사용된다
print("word[::-1] = ", word[::-1])