x = [1,2,3,4,5,6]
x.sort(reverse= False)
print(x)
a = sorted(x,reverse= True)
print(a)
b = x[-2:-1]
print(b)
y = [1,2,[3,4],5,6]
a,b,c,d,e,f = x
print(d)
a,b,c,d,e,f = f,e,d,c,b,a
print(b)
a,b,*rest = x
print(rest)
a,b,(c,d),e,f = y
print(c,d)