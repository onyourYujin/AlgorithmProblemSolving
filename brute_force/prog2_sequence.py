def solution(elements):
    result = set()
    cycle = elements * 2
    leng = len(elements)
    for i in range(leng):
        for j in range(leng):
            result.add(sum(cycle[j:j+i+1]))
    return len(result)