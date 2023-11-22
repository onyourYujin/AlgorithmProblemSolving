def solution(order):
    sub = []
    i = 1
    cnt = 0
    while len(order)+1 > i:  # 트럭에 상자를 실을 수 있는 경우
        sub.append(i)
        while sub and order[cnt] == sub[-1]:  # 보조 컨테이너에 실어야 하는 경우
            sub.pop()
            cnt += 1
        i += 1
    return cnt