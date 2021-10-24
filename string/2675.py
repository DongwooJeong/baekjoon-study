T = int(input())
for i in range(T):
    R, S = input().split()
    string = ""
    for i in S:
        string = string+i*int(R)
    print(string)
