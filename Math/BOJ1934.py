import math

n=int(input())
for _ in range(n):
    A,B = map(int,input().split())
    result = (A*B) // math.gcd(A,B)
    print(result)
    
# =========================================================================================
import math

n=int(input())
for _ in range(n):
    A,B = map(int,input().split())
    print(math.lcm(A,B))