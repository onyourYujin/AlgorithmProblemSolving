n=int(input())

for i in range(n):
    ox_list=list(input())
    cnt=0
    sum_cnt=0
    for ox in ox_list:
        if ox == "O":
            cnt+=1
            sum_cnt+=cnt
        else:
            cnt=0
    print(sum_cnt)
