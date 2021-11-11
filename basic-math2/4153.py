while True:
    a,b,c = map(int,input().split())
    if a==b==c==0:
        break
    elif max(a,b,c)==c and c**2==a**2+b**2:
        print("right")
    elif max(a,b,c)==a and a**2==b**2+c**2:
        print("right")
    elif max(a,b,c)==b and b**2==c**2+a**2:
        print("right")
    else:
        print("wrong")