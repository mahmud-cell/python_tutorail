x = [1, 2, 3 ,4 ,5 ,6,7,8,9,10]
print(len(x))
x.insert(len(x),11)
x.insert(len(x),12)
x.append(15)
x.extend([16,17,18,19,20])
print(x)
x.pop(17)
print(x)