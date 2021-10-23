N = int(input())
H = 0
for i in range(1,N+1):
    if i <= 99:
        H = H+1
    else:
        K = list(map(int,str(i)))
        if K[0]+K[2] == K[1]*2:
            H = H+1
print(H)
