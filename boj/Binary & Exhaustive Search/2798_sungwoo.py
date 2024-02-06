import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

result = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sumOfComb = cards[i] + cards[j] + cards[k]
            if sumOfComb <= m and sumOfComb > result:
                result = sumOfComb

print(result)