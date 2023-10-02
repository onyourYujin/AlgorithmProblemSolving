# from math import gcd

# def solution(arr):
#     answer = arr[0]
    
#     for i in arr[1:]:
#         answer = answer * i // gcd(answer, i)
    
#     return answer

# ================================

def gcd(n1,n2):
    num = n1 % n2
    if num == 0:
        return n2
    else:
        return gcd(n2, num)
    
def solution(arr):
    answer = 1
    for n in arr:
        answer = answer * n // gcd(answer, n)
    return answer