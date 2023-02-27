word=input().lower()
lst=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time=0

for i in range(len(word)):
    for j in lst:
        if word[i] in j:
            time+=lst.index(j)+3
print(time)
