def sosu(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return False
        return True
allnum = list(range(2,246912))
allsosu = []
for i in allnum:
    if sosu(i):
        allsosu.append(i)
while True:
    n = int(input())
    if n==0:
        break
    countnum=0
    for i in allsosu:
        if n<i<=n*2:   
            countnum+=1
    print(countnum)