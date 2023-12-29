# 1. set으로 푸는 방법
def solution(x, y, n):
    answer = 0
    s = {x} 
    
    while s:
        if y in s:
            return answer
        else:
            x = set()
            for i in s:
                if i+n <= y:
                    x.add(i+n) 
                if i*2 <= y:
                    x.add(i*2)
                if i*3 <= y:
                    x.add(i*3)
            s = x
            answer += 1
    return -1

# ==================================================================================
# 2. BFS로 푸는 방법
from collections import deque

def solution(x,y,n):
    queue = deque()
    queue.append((x,0))
    visited = set()

    while queue:
        i,j = queue.popleft()
        if i in visited:
            continue 
        if i == y:
            return j
        for s in (i+n, i*2, i*3):
            if s <= y and s not in visited:
                queue.append(s)
    return -1