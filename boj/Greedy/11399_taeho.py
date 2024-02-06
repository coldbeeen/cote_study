#시간 빠른 순으로 정렬해버리고 다 더해서 출력

n = int(input())

result = 0 

wating = list(map(int, input().split()))  # 대기열
wating.sort()

for i in range(1, n+1):
    result += sum(wating[0:i])
print(result)