alphabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time = 0
word = input()
for i in word:
    for j in alphabet:
        for k in j:
            if i==k:
                time+= alphabet.index(j)+3
print(time)

