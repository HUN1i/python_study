total = 0
count = 0

while True :
    n = int(input("정수 입력(0 : 종료)")) 

    if n == 0 :                          
        break                                   

    total += n                              
    count += 1                          
                                                
avg = total / count                                 
                            
print(f"\n합계 : {total} (= {avg:.1f})")




# 1회차)
# n = 123, rev = 0
# rev = 0 * 10 + 123 % 10
# = 0 + 3
#2회차)
# n = 12, rev = 3
#rev = 3 * 10 + 12 % 10
# 30 + 2
#3회차)
#n = 1, rev = 32

# rev = 32 * 10 + 1 % 10
# = 320 + 1

asd = 1

asd += 1

print (f"{asd}")