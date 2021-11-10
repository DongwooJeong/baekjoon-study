xone, yone=map(int, input().split())
xtwo, ytwo=map(int, input().split())
xthree, ythree=map(int, input().split())
listx = [xone, xtwo, xthree]
listy = [yone, ytwo, ythree]
for i in listx:
    if listx.count(i) == 1:
        xco = i
for i in listy:
    if listy.count(i) == 1:
        yco = i
print(xco, yco)
        