n_list = list(map(int,str(input())))
answer = []
for n in n_list:
    answer.append(int(n))
answer.sort(reverse=True)
print(int("".join(map(str, answer))))