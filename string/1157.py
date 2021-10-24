word = input().lower()
wordlist = list(set(word))
countword = []
for i in wordlist:
    K = word.count(i)
    countword.append(K)
if countword.count(max(countword))>1:
    print("?")
else:
    max_index = countword.index(max(countword))
    print(wordlist[max_index].upper())