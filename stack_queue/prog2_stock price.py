# 시간 초과, 2중 for문
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
    return answer

# ==================================================================================
from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        current_price = queue.popleft()
        count = 0
        
        for price in queue:
            count += 1
            if current_price > price :
                break
        answer.append(count)
    return answer

# ====================================================
def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break

    return answer