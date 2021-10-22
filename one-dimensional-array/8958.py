list=[]
N = int(input())
for i in range(N):
    list=input()
    sum=0
    bonus=1
    for i in list:
        if i =='O':
            sum=sum+bonus
            bonus=bonus+1
        else:
            bonus=1
    print(sum)