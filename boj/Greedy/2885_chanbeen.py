import sys

input = sys.stdin.readline

K = int(input())

times, choco, cnt = 0, 0, 0

while True:
    if 2 ** times >= K:
        choco = 2 ** times
        break
    times += 1

original = choco #K보다 큰 2의 최소 거듭제곱이 상근이가 구매해야할 초콜릿의 최소 크기

for _ in range(times):
    if K == choco: #상근이가 원하는 개수가 초콜릿 초기와 일치한다면 쪼갤 필요 없음
        break
    
    cnt += 1
    choco = int(choco/2) #초콜릿 쪼개기
    if K >= choco: 
        K -= choco
    #쪼개져 있는 초콜릿이 추가로 필요한 초콜릿보다 모양이 크다면 해결할 수 없음
    if K == 0:
        break #상근이가 필요한 개수를 만족했으면 반복문 조기 종료

print("%d %d" %(original, cnt))