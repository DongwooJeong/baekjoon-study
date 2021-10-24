S = list(input())
list_alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in list_alphabet:
    if i in S:
        print(S.index(i))
    else:
        print(-1)