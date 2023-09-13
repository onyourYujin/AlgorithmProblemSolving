N,M,K= map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
max1 = max(lst)
max2 = lst[N-2]


cnt = int(M/(K+1)) * K + (M %(K+1))

result = cnt * max1
result += (M-cnt) * max2

print(result)
