end=int(input())
main_li=[]
for i in range(0,end):
    x=str(input())
    li=x.split(" ")
    a=int(li[0])
    b=int(li[1])
    if (a+b > 6):
        main_li.append("Yes")
    else:
        main_li.append("No")
for i in range(0,end):
    print(main_li[i])        