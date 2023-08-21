N = int(input())
for _ in range(N):
    word = input()
    for y in range(len(word)-1):
        if word[y] == word[y+1]:
            pass
        elif word[y] in word[y+1:]:
            N-=1
            break
print(N)