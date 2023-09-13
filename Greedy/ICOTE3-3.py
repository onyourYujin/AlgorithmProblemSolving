m, n = map(int,input().split())
lst = []
for _ in range(m):
    arr = list(map(int,input().split()))
    min_arr = min(arr)
    lst.append(min_arr)

max_arr = max(lst)
print(max_arr)