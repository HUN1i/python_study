# set는 index가 없기 때문에 내장함수로 대부분 처리한다

# {}는 뒤에 배울 dictonary라는 타입이 사용한다



st = set() # 빈 set는 set() 타입으로 초기화해야 한다

print("st의 타입 :", type(st))

# add() : 요소를 추가
st.add(10)
st.add(20)
st.add(30)

st.add(10)          # 중복된 데이터는 에러가 아닌 무시

print("st =", st)

# remove : 지정한 요소를 제거
st.remove(20)
print("st =", st)


# update : 한번에 추가
st.update([100,200,300])
print("st =", st)