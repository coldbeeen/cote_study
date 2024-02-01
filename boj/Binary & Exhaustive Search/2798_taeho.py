import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
card = list(map(int, input().split()))

result = 0

# 브루트포스가 뭔지 바로 이해되는 문제
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            sum = card[i] + card[j] + card[k]
            
            if sum <= M:
                result = max(result, sum)
                
print(result)