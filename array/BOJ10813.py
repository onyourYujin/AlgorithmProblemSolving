#바구니 개수 M, 공 번호 M
N,M=map(int,input().split(' '))
basket=[str(i+1) for i in range(N)]

for exchange in range(M):
    i,j=map(int,input().split(' '))
    basket[i-1],basket[j-1]=basket[j-1],basket[i-1]

print(' '.join(basket))
