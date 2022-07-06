# 학생 5명의 점수를 일렬로 받아서 리스트에 저장
q = "5명 점수 : "
scores = list(map(int, input(q).split()))

print("scores =", scores)
plus = sum(scores)
avg =sum(scores)/len(scores)
print("합계: ",plus)
print("평균: ",avg)

print(f"1등: ",{max(scores)})
print("꼴등: ",{min(scores)})


total = 0
count = 0
mx = 0
mn = 99999
for sc in scores :
    total += sc
    count += 1

    if mx < sc :
        mx = sc
    if mn > sc:
        mn = sc

    
avg = total / count

print(f"합계 : {total}, (={avg:.1f})")

print(f"1등 : {mx}, 꼴등 : {mn}")


