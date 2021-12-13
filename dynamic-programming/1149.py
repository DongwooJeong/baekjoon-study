N=int(input())
lista = []
for i in range(N):
    lista.append(list(map(int, input().split())))
for i in range(1,N):
    lista[i][0]=min(lista[i-1][1],lista[i-1][2])+lista[i][0]
    lista[i][1]=min(lista[i-1][0],lista[i-1][2])+lista[i][1]
    lista[i][2]=min(lista[i-1][0],lista[i-1][1])+lista[i][2]
print(min(lista[N-1]))
