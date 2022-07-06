a = set([1,2,3,4,5,6])
b = set([4,5,6,7,8,9])
c = set([5,6,7,8,9,10])



I =a&b&c
U =a|b|c
D =a-b-c

print("교집합 :",I)
print("합집합 :",U)
print("차집합 :",D)

a=set([1,1,5,5,4,3,6,7,2,1,5,5,8,5])
a=list(set(a))
print("a=",a)

d=set([1,2,3,4,5,6])
e=set([4,5,6,7,8,9])
f=set([5,6,7,8,9,10])
e.remove(4)
e.remove(5)
f.remove(5)
f.update([1,2])
result = d-e-f
print("\nresult =",result)


print(d-e-f)
