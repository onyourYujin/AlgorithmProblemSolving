# 실패한 코드
def solution(n):
    answer = ''
    while n > 0:
        if n % 3 == 0:
            n = n // 3 - 1
            answer += '4'
        else:
            answer += str(r)
        n = n // 3

    return answer[::-1]

# ========================================================================================
def solution(n):
    answer = ''
    while n > 0:
        if n % 3 == 0:
            answer += '4'  # 마지막에도 몫은 추가하지 않고 나머지만 추가
            n = n//3 - 1  # 1,2,4만 있어야 하기 때문에
        else:
            answer += str(n%3)
            n //= 3
    return answer[::-1]