N=int(input())
lista = []
for i in range(N):
    lista.append(list(map(int, input().split())))
for i in range(1,N):
    for j in range(len(lista[i])):
        if j ==0:
            lista[i][j]=lista[i-1][j]+lista[i][j]
        elif j==len(lista[i])-1:
            lista[i][j]=lista[i-1][j-1]+lista[i][j]
        else:
            lista[i][j]=max(lista[i-1][j-1],lista[i-1][j])+lista[i][j]
print(max(lista[N-1]))