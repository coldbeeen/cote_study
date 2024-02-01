import sys
input = sys.stdin.readline


def combinations(i, cnt, comb):  # 모든 조합을 탐색하는 재귀 함수
    global n

    if cnt == 6:  # 6개의 수가 구성된 경우 출력 후 종료
        print(*comb)
        return

    # 현재 인덱스 위치를 저장하는 i의 역할이 중요 (요소가 중복되는 조합이 생기지 않음)
    # 1 2 3 4 7 에서는 더 이상 i가 이미 6이므로 for문 돌지 않아 그 다음으로 넘어감
    for idx in range(i, n):  # 차례대로 모든 경우의 수 시도
        comb.append(num_list[idx])
        combinations(idx + 1, cnt + 1, comb)  # 다음 인덱스로, 수의 개수 1 증가, comb 전달
        comb.pop()


while True:
    case = input().split()

    n = int(case[0])
    if n == 0:
        break
    num_list = list(map(int, case[1:]))

    combinations(0, 0, [])
    print()

