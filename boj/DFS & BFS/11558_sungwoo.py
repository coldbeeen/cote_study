import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    n = int(input())
    graph = [int(input()) for i in range(n)]  # 그래프 생성

    next_idx = 0  # 다음 지목될 사람의 인덱스 설정
    for i in range(n-1):  # n-1번 반복 (break 만나지 않았다면 주경이에게 도달하지 못하는 것임)
        next_idx = graph[next_idx] - 1  # 다음 사람의 인덱스를 구함
        if next_idx == n - 1:  # 주경이에게 도달했다면 i+1 출력
            print(i+1)
            break
    else:
        print(0)