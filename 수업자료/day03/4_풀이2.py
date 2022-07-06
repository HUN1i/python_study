a= int(input("정수1: "))
b= int(input("정수2: "))
c= int(input("정수3: "))

maximum = a

if maximum < b :
    maximum = b
if maximum < c :
    maximum = c

    

minimum = a
if minimum > b :
    minimum = b
if minimum > c :
    minimum = c
    print ("\n최댓값 :", maximum)
    print ("\n최솟값 =" ,minimum)
