# 정확도 낮은 코드
def is_prime(num):
    num = int(num)
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

from itertools import permutations
def solution(numbers):  # type(numbers) = str
    answer = []
    nums = numbers.split()
    prime = list(permutations(nums,2))
    for i in prime:
        nums.append("".join(i))
    for i in nums:
        if is_prime(i):
            answer += 1
    return answer

# =================================================================================================================
from itertools import permutations
def solution(numbers):
    answer = []
    nums = [n for n in numbers]  # nums = numers.split()
    per = []
    for i in range(1,len(numbers)+1):
        per+=list(permutations(nums,i))
    new_nums = [int(("").join(p)) for p in per]
    for i in new_nums:
        if is_prime(i):
            answer.append(i)
    return len(set(answer))