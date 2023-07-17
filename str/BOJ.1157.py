w = input().upper()
words = list(set(w))
cnt_list = []

for x in words:
    cnt = w.count(x)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list))>1:
    print("??")
else: 
    max_index = cnt_list.index(max(cnt_list))
    print(words[max_index])
