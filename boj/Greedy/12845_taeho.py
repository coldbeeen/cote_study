import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))

card.sort(reverse=True)

x = card[0]
gold = 0

for i in range(1, len(card)):
    gold += (x + card[i])

print(gold)