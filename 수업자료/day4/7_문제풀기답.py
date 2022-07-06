

for i in range(5):
    for j in range (4-i):
        print(" ", end = "")
    for j in range(i*2+1):
        print("*", end ="" )
    print()
n = int(input("입력 : "))
for i in range(n) :
    for j in range(n):
        print(f"*", end= "")
    print()


print()



for i in range(n) :
    for j in range(i+1):
        print(f"*", end= "")
    print()   

print()

for i in range(n) :
    for j in range(n - i):
        print("*", end= "")   
print()

for i in range(n) :
    for j in range(n-1-i):
        print(" ", end= "")
    
    for j in range (i + 1) :
        print("*", end = "")   
print()

for i in range(5) :
    for j in range(4-i):
        print("", end = "")
print()





for i in range(5) :
    for j in range(i) :
        print(" ", end = "")
print()