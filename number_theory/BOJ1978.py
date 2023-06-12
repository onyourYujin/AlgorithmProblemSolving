N = int(input())
N_list = list(map(int,input().split()))
cnt = 0

for x in N_list:
    for y in range(2,x+1):
        if x%y == 0:
            if y==1 or y==x:
                cnt+=1
            break
print(cnt)