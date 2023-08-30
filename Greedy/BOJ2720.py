N = int(input())
for _ in range(N):
    change = int(input())
    a=change//25
    b=(change-(a*25))//10
    d=(change-(a*25)-(b*10))
    if d>=5:
        c = 1
    else:
        c = 0
    print(a,b,c,d-(c*5))