N, K = map(int, input().split())

result = 0
n = 0

for i in range(1, N + 1):
    if N % i == 0:
        n += 1

    if n == K: # K번째 약수가 됐을 때
        result = i
        break

print(result)