import sys

input = sys.stdin.readline

N, K = map(int, input().split())

divisor = []

for i in range(1, N + 1):
    if N % i == 0:
        divisor.append(i) #약수 저장

if len(divisor) < K: #개수가 적으면 0 출력
    print(0)
else:
    print(divisor[K-1])