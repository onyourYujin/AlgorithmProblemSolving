# 정답이지만 시간 초과인 코드(완전 탐색)
# 시간 복잡도 : O(n2)
def solution(numbers):
    answer = [-1] * len(numbers)
    for idx,i in enumerate(range(len(numbers))):
        for j in range(idx+1,len(numbers)):
            if i<j:
                answer[i] = numbers[j]
                break
    return answer

# =====================================================================================
# 스택을 이용한 풀이
def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    for idx, num in enumerate(numbers):
        while stack and numbers[stack[-1]]<num:
            answer[stack.pop()] = num
        stack.append(idx)
    return answer