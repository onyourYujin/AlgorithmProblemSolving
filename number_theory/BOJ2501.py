N,K=map(int,input().split())
lst = []

for x in range(1,N+1):
    if N%x == 0:
        lst.append(x)
lst.sort()
if len(lst)<K:
    print(0)
else:
    print(lst[K-1])