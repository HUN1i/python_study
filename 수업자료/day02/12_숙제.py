# 05. 포매팅PDF 마지막 페이지 문제를 풀어온다
kor = int(input("국어 : "))
eng = int(input("영어 : "))
mat = int(input("수학 : "))

total = kor + eng + mat
avg = total/3

print(f"\n국 {kor}, 영 {eng}, 수 {mat}")
print(f"합계 : {total} (= {avg:.2f})")