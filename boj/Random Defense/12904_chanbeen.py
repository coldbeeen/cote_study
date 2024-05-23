import sys

input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

flag = 0

while T:
    if T[-1] == 'A': #마지막에 A가 추가됐었으면
        T.pop()
    elif T[-1] == 'B': #마지막에 B가 추가됐었으면
        T.pop()
        T.reverse() #pop 먼저하고 뒤집는 게 포인트
    
    if S == T:
        flag = 1
        break

print(flag)

#재귀 호출로 모든 경우를 시도하면 시간 초과 발생
#S를 T로 만들려고 하다보니 경우의 수가 너무 많아지는 듯
#T를 S로 만드는 역연산을 해보자