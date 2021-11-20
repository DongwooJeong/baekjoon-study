row, column = map(int, input().split())
color = []
err = []
for i in range(row):
    color.append(input())

for a in range(row-7):
    for b in range(column-7):
        err1=0
        err2=0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j)%2==0:
                    if color[i][j]!='W':
                        err1+=1
                    else:
                        err2+=1
                else:
                    if color[i][j]!='B':
                        err1+=1
                    else:
                        err2+=1
        err.append(err1)
        err.append(err2)

print(min(err))