x = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10]
y = [1, 2, [3, 4, 5, 6], 7 , 8, 9, 10]
a,b,c,d,e,f,g,h,i,j = x
print(a,b,c)
a,b,c,d,e,f,g,h,i,j = j,i,h,g,f,e,d,c,b,a
print(a,b,c)
a,b,*rest= x
print(rest)
a,b,(c,d,e,f),*rest = y
print(c,d,e,f)