def solution(stones, k):

    answer, l, r = 0, 0, max(stones)

    # 이분 탐색 수행
    while l <= r:
        m = (l+r) // 2

        consecutive_cnt = 0

        # 모든 돌을 순회하며 m명이 지나갈 때 연속된 k개의 돌을 지나갈 수 있는지 검사
        for stone in stones:
            if stone - m < 0:
                consecutive_cnt += 1

                if consecutive_cnt == k:
                    break

            else:
                consecutive_cnt = 0

        else:
            # 모두 징검다리를 건널 수 있다면 위쪽 범위 탐색 및 answer 값 갱신
            l = m + 1
            answer = m
            continue

        # 모두 못 건넌다면 왼쪽 범위 탐색
        r = m - 1

    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))