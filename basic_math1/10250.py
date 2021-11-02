T=int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    K=1
    F=0
    if N%H==0:
        K=N//H
        print(H*100+K, sep='')
    else:
        K+=N//H
        F+=N%H
        print(F*100+K, sep='')