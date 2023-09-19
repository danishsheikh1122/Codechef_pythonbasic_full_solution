end=int(input())
li=[]
for i in range(0,end):
    patties,buns=map(int,input().split())
    li.append(min(patties,buns))
for i in range(0,end):
    print(li[i])
    