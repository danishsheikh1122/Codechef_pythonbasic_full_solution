end=int(input())
main_li=[]
for i in range(0,end):
    x,y=map(int,input().split())   
    res=x*y
    main_li.append(res)
for i in range(0,end):
    print(main_li[i])