import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coin = []
cnt = 0
idx = N - 1

for i in range(N):
    c = int(input())
    coin.append(c) #코인 리스트 생성

while idx >= 0:
    if K // coin[idx] == 0:
        idx -= 1
        continue
    cnt += K // coin[idx]
    K = K % coin[idx]
    idx -= 1 #큰 금액부터 동전 개수 카운트

print(cnt)