# {}의 기능
# {index : 기능}

name = "홍길동"
age = 25

print("이름 : {}, 나이 : ()".format(name, age))
#                                    0     1 (= index, 순서번호)

# index를 사용하면 원하는 위치에 채울 수 있다~
print("이름 : {0}, 나이 : {1}".format(name, age))
print("이름 : {1}, 나이 : {0}".format(name, age))
print("이름 : {1}, 나이 : {1}".format(name, age))
height = 170.123456

print("신장 : {}cm".format(height))
print("신장 : {:.2f}".format(height))
# 기능을 사용할 땐  index를 쓰지 않도라도 무조건 : 을 작성한다!!!

print("신장 : {0:.2f}cm,{0:.4f}cm".format(height))
# index와 기능을 같이 쓸 땐 : 을 기준으로 구분한다
# - 조금 지저분하게 되기 때문에 어렵다면 나중에 익히도록 한다

