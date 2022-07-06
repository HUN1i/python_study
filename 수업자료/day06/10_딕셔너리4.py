# 딕셔너리 요소 추가, 수정, 삭제

dt = {}     # 빈 {}는? 딕셔너리
print("dt=", dt)
# 1.추가: 없는 key값에 value를 대입하면 추가된다
dt['c언어']= 70
dt['Python'] = 90
dt['java'] = 75

print("dt =", dt)
#
# 2. 수정 : 이미 있는 key 값에 value를 대입하면 수정된다
# key 값은 중복이 되지 않기 때문.
dt['c언어'] = 80

print("dt =", dt)   

# 3. 삭제 : 내장 함수를 사용
dt. pop('Java')
print("dt =", dt)