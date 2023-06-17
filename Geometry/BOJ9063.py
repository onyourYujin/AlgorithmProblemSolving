n=int(input())
width = []
length = []
for i in range(n):
    a,b = map(int,input().split())
    width.append(a)
    length.append(b)
print((max(width)-min(width))*(max(length)-min(length)))