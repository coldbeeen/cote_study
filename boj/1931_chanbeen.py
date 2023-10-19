import sys

input = sys.stdin.readline

N = int(input())

time = []
for i in range(N):
    tmp = list(map(int, input().split()))
    time.append(tmp)

time = sorted(time, key = lambda x: (x[1], x[0])) #끝나는 시간이 이른 순으로 정렬

result = []
result.append(time[0])
idx = 0

for i in range(1, len(time)):
    if result[idx][1] <= time[i][0]: #지난 회의가 끝나고 다음 회의가 시작할 수 있으면
        result.append(time[i])
        idx += 1

print(len(result))