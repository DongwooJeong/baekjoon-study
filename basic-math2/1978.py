N=int(input())
nonprime=[]
prime = [int(x) for x in input().split()]
for i in prime:
    for j in range(2,i):
        if i%j==0:
            nonprime.append(i)
nonprime.append(1)
prime=list(set(prime)-set(nonprime))
print(len(prime))
