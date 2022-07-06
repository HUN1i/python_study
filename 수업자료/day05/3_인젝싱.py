word = "welcome to python" 
#       012345678901234567 #= index, 순서 번호
#index  = 색인

print("word[11] =", word[11])
# - index를 활용한 데이터 참조 방식을 'indexing'라고 한다.

print("word[8] =", word[8], "\n")

for i in range(18):
    print(f"word[{i}]= {word[i]}")


    # python은 index가 음수로도 매겨져 있다
    # 가장 뒤부터 -1 에 해당

print("\nword[-1] =", word[1])

# 문자열과 사용하면 좋은 함수(=기능)
# len("문자열") : 문자열의 문자 개수를 반환

n = len(word)

print("word의 길이 :", n)