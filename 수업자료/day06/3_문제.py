
scores = []


# 1. 빈 리스트를 선언

# 2. 반복을 활용해서 5명의 학생의 점수를 입력받고 리스트에 "추가"
for i in range(5) :
    n = int(input(f"{i + 1}번째 점수 :"))
    scores.append(n)


# 3. 2번의 리스트를 출력
print("\n점수 목록)")
print(scores)
# 4. 2번의 리스트를 내림차순으로 정렬해서 성적순으로 출력
scores.sort(reverse=True)
print("\n성적순)")
print(scores)
#5. 1등과 꼴등 출력
n = len(scores)
print("\n1등 :", scores[0])
print(f"{n}등 : {scores[n-1]}")