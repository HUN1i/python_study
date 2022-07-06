import random

n = random.randint(1, 10)   # 1~10 사이의 무작위 수를 반환
print("n =", n)

# 위의 코드를 참고해서 로또 추첨을 구현해 보자~
# 규칙)
# 1. 1~45 사이의 무작위 수를 뽑는다
# 2. 숫자는 6개를 뽑고 중복이 되지 않는다
# 3. 결과 발표시 항상 작은 순에서 큰 순으로 번호를 발표한다


lotto=set()


    
while len(lotto) !=6: #len: 문자열 길이 반환      #set이 6개가 될때까지. 즉 중복없이 6개
    n = random.randint(1,45)    
    lotto.add(n)
lotto = list(lotto)
lotto.sort()#sort: 정렬(list에서만 사용)
print(lotto)