import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

card = list(map(int, input().split()))

blackjack = list(combinations(card, 3)) #조합 경우의 수 생성

for i in range(len(blackjack)):
    amount = 0
    
    for j in range(len(blackjack[i])):
        amount += blackjack[i][j]
        
    blackjack[i] = amount #3개 카드 값을 더한 값으로 값 갱신

blackjack.sort()

answer = [x for x in blackjack if x <= M] #최대값보다 작은 애들만 담기

print(answer[-1]) #그 중 최대