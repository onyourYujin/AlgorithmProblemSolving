def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    for i in range(n, 0, -1):
        cnt = 0
        for citation in citations:
            if citation >= i:
                cnt += 1
        if cnt >= i:
            return i
    return 0