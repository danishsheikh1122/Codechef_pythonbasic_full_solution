end=int(input())
li=[]
for i in range(0,end):
    a,b=map(int,input().split())
    res=max(a,b)
    if(res== a):
        li.append("A")
    elif(res==b):
        li.append("B")
    else:
        print("invalid input")
for i in range(0,end):
    print(li[i])    