end=int(input())
li=[]
for i in range(0,end):
    chef_son_height,minimum_height_required=map(int,input().split())
    if(chef_son_height >= minimum_height_required):
        li.append("Yes")    
    else:
        li.append("No")    
for i in range(0,end):
    print(li[i])