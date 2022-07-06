address = "부산광역시 수영구 민락동"
        #  0 1 2 3 4 5 6 7 8 9 0 1 2
si = address[0:6]
goo = address[5:9]
dong = address[9:]
print (f"""시 :{si}구: {goo} 동 : {dong}""")

say ="I love Pusan"


say =say[:7] + "B" + say[8:]

print("say =", say)