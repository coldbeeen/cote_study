# 끝나는 시간 기준으로 정렬해서
# 이전팀 끝나는 시간 - 다음팀 시작시간 계산
# 다음팀 end_time 저장
import sys
input = sys.stdin.readline

N = int(input())

time = [[0]*2 for _ in range(N)]
for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    time[i][0] = start
    time[i][1] = end

# sort에서 lambda 쓰는 법 숙지해두기
time.sort(key = lambda x: (x[1], x[0]))

cnt = 1

end_time = time[0][1]

for i in range(1, N):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)