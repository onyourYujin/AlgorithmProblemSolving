def solution(n):
    arr = [1,2]
    for i in range(2,n):
        arr.append((arr[i-2]+arr[i-1]) % 1000000007)  # 시간초과 방지 :계산 결과를 작은 값으로 유지하여 정확도를 향상
    return arr[-1]