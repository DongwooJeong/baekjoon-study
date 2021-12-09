import sys
zero = [1,0,1]
one=[0,1,1]
def fbo(num):
    length=len(zero)
    if length<=num:
        for i in range(length,num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    return print(zero[num], one[num])

T=int(sys.stdin.readline())
for i in range(T):
    N=int(sys.stdin.readline())
    fbo(N)