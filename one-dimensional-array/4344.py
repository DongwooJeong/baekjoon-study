C = int(input())
for i in range(C):
    N = list(map(int, input().split()))
    K = N.pop(0)
    A = sum(N)/len(N)
    Z=0
    for i in N:
        if i > A:
            Z=Z+1
    T=Z/K
    P="{:.3%}".format(T) 
    print(P)
    

