# 시간초과 코드
def solution(people, limit):
    cnt = 0
    people.sort()
    while len(people)>0:
        if people[0] + people[-1] > limit:
            people.pop()
            cnt += 1
        else:
            people.pop()
            if len(people)>0:
                people.remove(people[0])
            cnt += 1
    return cnt

# ===========================================================================

def solution(people,limit):
    cnt = 0
    people.sort()
    left, right = 0, len(people)-1
    while left <= right:
        if people[left] + people[right] <= limit:
                left += 1
        right -= 1
        cnt += 1
    return cnt