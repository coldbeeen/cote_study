import sys
import heapq 

input = sys.stdin.readline

N = int(input())

cards = []

for i in range(N):
    heapq.heappush(cards, int(input()))

result = 0

while len(cards) > 1:
    num1 = heapq.heappop(cards)
    num2 = heapq.heappop(cards)
    
    result += num1 + num2
    
    heapq.heappush(cards, num1 + num2)

print(result)

#먼저 연산되는 수는 이후에도 계속 연산된다
#따라서 작은 수를 먼저 연산시키는 것이 최소 비교이다
#매 반복마다 가장 작은 수 2개를 뽑아서 비교하는 것이 중요
#반복문마다 sort하면 시간 초과 발생
#힙 정렬을 사용해야 하나?

#힙 정렬을 사용해야 풀리는 간단한 그리디 문제