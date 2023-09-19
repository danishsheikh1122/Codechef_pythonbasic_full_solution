txt = str(input())

x = txt.split(" ")
a=int(x[0])
b=int(x[1])
if(a == b*2 ):
    print("Yes")
else:
    print("No")
