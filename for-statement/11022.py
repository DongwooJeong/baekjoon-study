import sys
for i in range(1,int(sys.stdin.readline())+1):
    A, B = map(int,sys.stdin.readline().split())
    print("Case","#"+str(i)+":", A,"+",B,"=",A+B)