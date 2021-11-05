M=int(input())
N=int(input())
prime=[]
nonprime=[]
for i in range(M,N+1):
    prime.append(i)
    for j in range(2,i):
        if i%j==0:
            nonprime.append(i)
nonprime.append(1)
A=list(set(prime)-set(nonprime))
if len(A)>0:
    print(sum(A))
    print(min(A))
else:
    print(-1)
