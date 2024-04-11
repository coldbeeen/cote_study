import sys

def abs_diff(a, b):
    return abs(a-b)

def DFS(num, S, B):    
    global result

    # 해당하는 경우의 신맛, 쓴맛을 불러오고 앞에 까지 조합에 곱과 합을 해준다
    s, b = SB[num][0], SB[num][1]
    S *= s
    B += b

    diff = abs_diff(S, B)
    result = min(result, diff)

    for i in range(num, N):
        # 다음 경우의 수를 확인하러 넘어간다
        DFS(i+1, S, B)


N = int(sys.stdin.readline())

SB = [[]]
for i in range(N):
    s, b = map(int, input().split())
    
    # 신맛, 쓴맛 리스트로 저장
    row = [s, b]
    SB.append(row)


result = float("inf")

# 모든 경우를 시작점으로 삼고 경우의 수 조회
for i in range(N):
    DFS(i+1, 1, 0)

print(result)

"""
문제:

N개의 신맛, 쓴맛 S, B를 받고 각 재료 조합 차의 최솟값 구하기.
신맛은 곱, B는 합
___________________________________________________________________
풀이:

DFS 구조로 모든 경우의 수를 탐색하며 최소 경우의 수를 찾았다.
백트래킹이란 것을 공부했는데 이게 백트래킹을 사용해 푼건지 헷갈린다.
"""