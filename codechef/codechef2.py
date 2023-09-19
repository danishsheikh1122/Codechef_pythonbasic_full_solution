x=str(input())
li=x.split(" ")
a=int(li[0])
b=int(li[1])
res=a+b+(a*b)
if(res==111):
    print("Yes")
else:
    print("No")