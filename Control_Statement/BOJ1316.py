N = int(input())
cnt = N
for x in range(N):
    word = input()
    new = set(word)
    for y in range(len(word)-1):
        if word[y] == word[y+1]:
            pass
        elif word[y] in word[y+1:]:
            cnt-=1
            break
print(cnt)