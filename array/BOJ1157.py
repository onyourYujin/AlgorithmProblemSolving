word = input().upper() 
new_word = list(set(word))
result = []
for x in new_word:
    cnt = word.count(x)
    result.append(cnt)
if result.count(max(result))>=2:
    print("?")
else:
    print(new_word[result.index(max(result))])