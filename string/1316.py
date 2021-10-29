N = int(input())
count_num = 0
for i in range(N):
    duplicate = 0
    words = input()
    for j in range(len(words)-1):
        if words[j] != words[j+1]:
            next = words[j+1:]
            if next.count(words[j])>0:
                duplicate+=1
    if duplicate ==0:
        count_num += 1
print(count_num)
            
