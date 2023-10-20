def solution(elements):
    result = set()
    cycle = elements * 2
    leng = len(elements)
    for i in range(leng):  # 몇 개의 연속된 수열을 합칠 지 결정
        for j in range(leng):  # 부분 수열의 시작 위치
            result.add(sum(cycle[j:j+i+1]))
    answer = len(result)
    return answer