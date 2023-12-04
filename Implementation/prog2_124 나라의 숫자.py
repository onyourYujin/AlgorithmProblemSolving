# def solution(n):
#     answer = ''
#     while n > 0:
#         if n % 3 == 0:
#             n = n // 3 - 1
#             answer += '4'
#         else:
#             answer += str(r)
#         n = n // 3

#     return answer[::-1]

def solution(n):
    answer = ''
    while n > 0:
        if n % 3:
            answer += str(n % 3)
            n //= 3
        else:
            answer += "4"
            n = n//3 - 1
    return answer[::-1]