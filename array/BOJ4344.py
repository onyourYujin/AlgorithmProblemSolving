n=int(input())

for i in range(n):
    score=list(map(int,input().split()))
    avr=sum(score[1:])/score[0]
    cnt=0
    for j in score[1:]:
        if j>avr:
            cnt+=1
    rate=(cnt*100)/score[0]
    print(f"{rate:3f}%")