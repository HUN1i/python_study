# 중첩 반복문 : 반복문 안에 반복문을 구성하는 방식



for i in range (1, 4) : #  행(=줄)반복
    print(f"{i} : ", end = " ")
    for j in range(1,6) :# 열(=데이터) 반복
        print(j, end = " ")
    print()


# 맨위는 줄반복이라서 내부까지 다 반복하고 안에 들은거는 자기꺼 또 반복함