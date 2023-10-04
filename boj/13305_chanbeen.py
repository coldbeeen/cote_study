import sys

input = sys.stdin.readline

N = int(input())

road = list(map(int, input().split()))
oil = list(map(int, input().split()))

result = 0
cheap = oil[0] #출발 시의 기름값을 가장 싸다고 초기화

for i in range(N - 1):
    if cheap >= oil[i + 1]: #다음 도시가 더 싸면
        result += cheap * road[i] #현재 도시 넘어갈 만큼만 주유
        cheap = oil[i + 1] #최저가 기름값 갱신
    
    else: #다음 도시가 더 비싸면
        result += cheap * road[i] #더 싼 도시가 나올때까지 주유

print(result)