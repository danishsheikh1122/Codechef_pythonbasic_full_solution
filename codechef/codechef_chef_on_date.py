end=int(input())
li=[]
for i in range(0,end):
    chef_took_dollars_with_him,total_dollar_to_pay=map(int,input().split())
    if(chef_took_dollars_with_him >= total_dollar_to_pay):
        li.append("YES")
    else:
        li.append("NO")
        
for i in range(0,end):
    print(li[i])