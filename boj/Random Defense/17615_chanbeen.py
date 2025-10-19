#약 70분 소요, 15 ~ 17번째 줄 로직 구글링

N = int(input())

bs = list(input().rstrip())

answer = []

red = 0
blue = 0
cnt = 0

for i in range(N): #우측으로 빨간 공 보내기
    if bs[i] == 'R':
        red += 1
    
    if bs[i] == 'B' and red: #연속이 끊겼을 때만 갱신
        cnt += red #연속된 빨간 공 그룹은 안 더해지는 전략
        red = 0 

answer.append(cnt)

cnt = 0

for i in range(N): #우측으로 파란 공 보내기
    if bs[i] == 'B':
        blue += 1
    
    if bs[i] == 'R' and blue:
        cnt += blue
        blue = 0

answer.append(cnt)

bs.reverse() #좌측으로 공 보내기

cnt = 0
red = 0
blue = 0

for i in range(N):
    if bs[i] == 'R':
        red += 1
    
    if bs[i] == 'B' and red:
        cnt += red
        red = 0
        
answer.append(cnt)

cnt = 0

for i in range(N):
    if bs[i] == 'B':
        blue += 1
    
    if bs[i] == 'R' and blue:
        cnt += blue
        blue = 0

answer.append(cnt)

print(min(answer))

#R 또는 B 둘 중 하나만 움직여서 같은 색깔끼리 모을 수 있는 최소 횟수
#1. R 다 왼쪽으로 보내기
#2. R 다 오른쪽으로 보내기
#3. B 다 왼쪽으로 보내기
#4. B 다 오른쪽으로 보내기