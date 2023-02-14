N=int(input())
for x in range(N):
    num,ltr=input().split()
    result=''
    for i in ltr:
        i=int(num)*i
        result+=i
    print(result)
