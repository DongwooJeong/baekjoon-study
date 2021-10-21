A = int(input())
B = int(input())
C = int(input())
N = A*B*C
X = [int(a) for a in str(N)]
for i in range(10):
    K = X.count(i)
    print(K)