N=int(input())
my_list=list(map(int,input().split()))
min=my_list[0]
max=my_list[0]

for i in my_list[1:]:
    if min>=i:
        min=i
    elif max<=i:
        max=i
print(min, max)
