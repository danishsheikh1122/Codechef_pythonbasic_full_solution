end=int(input())
main_list=[]
for i in range(0,end):        
    x=str(input())
    li=x.split(" ")
    a=int(li[0])
    b=int(li[1])
    main_list.append(a+b)
print("\n")
for i in range(0,end):
    print(main_list[i])
    