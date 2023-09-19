end=int(input())

li=[]

for i in range(0,end):
    number_of_pages,number_of_words_per_page=map(int,input().split())
    res=number_of_pages*number_of_words_per_page
    li.append(res)
for i in range(0,end):
    print(li[i])