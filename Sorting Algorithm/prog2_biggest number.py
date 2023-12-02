# 실패한 코드
def solution(numbers):
    sorted_num = sorted(numbers, key=lambda x: str(x)[0])
    sorted_num.reverse()
    return str(int("".join(sorted_num)))
# ========================================================================================
def solution(numbers):
    sorted_num = list(map(str, numbers))
    sorted_num.sort(key=lambda x: x*3, reverse=True)  # str 비교할 때, 각 자리의 문자를 비교, 판단
    return str(int("".join(sorted_num)))