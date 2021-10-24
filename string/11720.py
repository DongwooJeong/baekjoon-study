N = int(input())
list_num=list(map(str, input()))
list_sum=[]
for n in list_num:
    list_sum.append(int(n))
print(sum(list_sum))