from collections import Counter

def solution(k, tangerine):
    answer = 0
    count = sorted(Counter(tangerine).items(),reverse=True, key=lambda x:x[1])
    # lambda -> 튜플의 두번째 값(x[1])을 기준으로 sort 한다는 뜻

    for key, value in count:
        if k <= 0 :
            break
        k -= value
        answer += 1
    return answer