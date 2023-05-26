N_list,M_list = [],[]
N,M = list(map(int,input().split()))

for row in range(N):
    row = list(map(int,input().split()))
    N_list.append(row)
for row in range(N):
    row = list(map(int,input().split()))
    M_list.append(row)

for row in range(N):
    for column in range(M):
        print(N_list[row][column]+M_list[row][column],end=' ')
    print()