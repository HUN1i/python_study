# Python의 print()문은 자동으로 마지막에 줄바꿈(\n)이 들어감

print("Hello") # Hello를 출력 후 자동으로 마지막에 \n이 들어감
print("World\n")

print("Hello", end="★")
print("World")

# print()에는 end라는 옵션이 있고
# 작성하지 않으면 자동으로 \n이 채워지게 만들어짐

# 이 때, 직접 작성하면 작성한 문자가 마지막에 출력된다