x,y,w,h = map(int,input().split())
list = [(w-x),(h-y),x,y]
print(min(list))