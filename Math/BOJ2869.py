A,B,V = map(int,input().split())
n=0
day=0
while n<V:
    day+=1
    n+=A
    n-=B
print(day)