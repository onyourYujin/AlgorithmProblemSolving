import sys
n = (int(input()))
x = []
for i in range(n):
    x.append(int(sys.stdin.readline()))
for j in sorted(x):
    print(j)