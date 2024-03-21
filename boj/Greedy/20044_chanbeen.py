import sys

input = sys.stdin.readline

n = int(input())
student = list(map(int, input().split()))
student.sort() #코딩 역량 순으로 정렬

team_power = [0] * n

for i in range(n):
    team_power[i] = student[i] + student[2 * n - i - 1] 
    #가장 강한 사람과 가장 약한 사람을 한 팀으로 하는 것이 가장 일정

print(min(team_power))