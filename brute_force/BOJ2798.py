from itertools import combinations

N,M = map(int,input().split())
cards = list(map(int,input().split()))
num = 0

for card in combinations(cards, 3):
    temp_sum = sum(card)
    if num < temp_sum <= M:
        num = temp_sum
print(num)