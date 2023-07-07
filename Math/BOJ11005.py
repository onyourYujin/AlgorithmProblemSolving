N,B = input().split()
base = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
li=[]
new_li=[]

while True:
    a=int(N) % int(B)
    li.append(a)
    N=int(N) // int(B)

    if N == 0: 
        break
for i in li:
    for j in base:
        if j==base[i]:
            new_li.append(j)
for x in new_li:
    print(x,end="")