N=int(input())
a = 0
b = 0
while b<N:
    a+=1
    b=a+b
A=0
B=a+1
for i in range(N+a-b):
    A=A+1
    B=B-1
if (A+B)%2!=0:
    print(A,'/',B, sep='')
else:
    print(B,'/',A, sep='')