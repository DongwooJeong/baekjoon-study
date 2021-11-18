N=int(input())
result = 0
for i in range(1,N+1):
    jaritsoo = list(map(int,str(i)))
    result = i+sum(jaritsoo)
    if result==N:
        print(i)
        break
    if i==N:
        print(0)

