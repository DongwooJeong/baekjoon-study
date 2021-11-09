x,y,w,h = map(int, input().split())
listlen = []
listlen.append(h-y)
listlen.append(y)
listlen.append(w-x)
listlen.append(x)
print(min(listlen))