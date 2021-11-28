import sys
sentence=[]
N=int(sys.stdin.readline())
for i in range(N):
    sentence.append(sys.stdin.readline())
set_sentence=set(list(sentence))
sentence=list(set_sentence)
sentence.sort()
sentence.sort(key=len)
for i in sentence:
    print(i, end='')
