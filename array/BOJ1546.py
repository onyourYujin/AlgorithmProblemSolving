N=int(input())
a=list(map(int,input().split()))
M_score=max(a)
arr=[]

for i in a:
    arr.append(float(i/(M_score*100)))
print((sum(arr)/N)*10000)
