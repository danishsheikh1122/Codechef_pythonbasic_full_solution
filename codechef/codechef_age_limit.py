end=int(input())
main_li=[]
for i in range(0,end):
    x=str(input())
    li=x.split(" ")
    age_shoud_be_greater_than=int(li[0])
    age_shoud_be_less_than=int(li[1])
    age_of_chef=int(li[2])
    if(age_of_chef >= age_shoud_be_greater_than and age_of_chef < age_shoud_be_less_than):
        main_li.append("Yes")
    else:
        main_li.append("No")
        
for i in range(0,end):
    print(main_li[i])
        