from collections import deque

def solution(priorities, location):
    answer = [] # 이미 실행된 프로세스
    queue = deque((idx, priority) for idx, priority in enumerate(priorities))
    while queue:  # queue가 비어 있지 않는 동안 반복  
        process = queue.popleft()  # (idx, priority)
        if any(process[1]<q[1] for q in queue):  # q[1] => priority, Boolean type로 반환
            queue.append(process) # 자기보다 큰 수가 있으면 queue의 맨 뒤로 다시 배치
        else:
            answer.append(process) # 자기가 제일 크면 answer로(이미 실행된 프로세스)
            
    for i in answer:
        if i[0] == location:  # i[0] => queue의 index
            return answer.index(i)+1