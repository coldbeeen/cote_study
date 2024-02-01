import sys

input = sys.stdin.readline

N = int(input())

people = [list(map(int, input().split())) for i in range(N)]

for i in range(N):
    rank = 1
    
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1 #몸무게 키 둘 다 커야 덩치가 크다고 정의
    
    print(rank, end = ' ')