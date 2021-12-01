N=int(input())
num=list(map(int,input().split()))

num2=sorted(list(set(num)))
dictnum={num2[i]: i for i in range(len(num2))}

for i in num:
    print(dictnum[i], end=' ')