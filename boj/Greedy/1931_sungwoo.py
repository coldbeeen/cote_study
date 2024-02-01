import sys
input = sys.stdin.readline

n = int(input())
meetings = [list(map(int, input().split())) for i in range(n)]
meetings.sort(key=lambda x: x[0])  # 시작 시간 기준 정렬! (4시부터 4시까지의 회의를 회의로 쳐야하는 이상한 반례 때문에 추가)
meetings.sort(key=lambda x: x[1])  # 종료 시간 기준 정렬!

prev_end_time, result = 0, 0
for meeting in meetings:
    if meeting[0] >= prev_end_time:  # 회의 가능!
        result += 1
        prev_end_time = meeting[1]  # 다음 회의 가능 여부 판별을 위해 직전 회의의 종료 시간 기록


print(result)

"""
반례를 보아하니
상당히 더러운 문제임
2
4 4
2 4
1
"""