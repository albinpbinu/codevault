k=[2,0,4,3,0,7,0,6,7,0,3]
for i in k:
    if i==0:
        k.remove(i)
        k.append(i)
print(k)
