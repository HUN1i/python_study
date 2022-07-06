# 리스트와 사용하면 좋은 함수들
# 1. len(): 리스트의 요소 개수를 반환
# 2. sum(): 리스트 요소의 합계를 반환
# 3. max(): 리스트 요소 중 최대값을 반환
# 4. min(): 리스트 요소 중 최소값을 반환

li = [70,10,90,80,60,20,30]

n = len(li)
print("li의 개수 :", n)

total = sum(li)
print("li의 합계 :", total)

mx = max(li)
print("li의 최대 :",mx)

mn = min(li)
print("li의 최소 :", mn)

avg = sum(li) / len(li)
print("li의 평균 :", avg)
