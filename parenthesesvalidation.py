t="([])"
stack=[]
flag=True
d={')':'(',']':'[','}':'{'}
for i in t:
    if i in "({[":
        stack.append(i)
    elif i in ")]}":
        if not stack or stack[-1]!=d[i]:
            flag=False
            break
        stack.pop()
if flag:
    print("True")
else:
    print("False")
