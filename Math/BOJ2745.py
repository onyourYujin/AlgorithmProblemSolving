N,B = input().split()
base = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result=0
for i, x in enumerate(N):
    for j, y in enumerate(base):
        if x == y:
            cnt=j
            break
    res+=cnt*(int(B) ** (len(N)-i-1))
print(result)