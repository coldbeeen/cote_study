# 12분
import heapq


def solution(s, K):
    answer = 0

    heapq.heapify(s)
    # 음식이 남아있을 동안
    while s:
        # 제일 안 매운거
        first = heapq.heappop(s)

        # 제일 안매운게 K보다 높으면 나머지는 다 K보다 높음
        if first >= K:
            return answer

        if s:
            second = heapq.heappop(s)
            new = first + 2 * second
            heapq.heappush(s, new)
            answer += 1
        # 제일 안 매운거 뽑았는데, 힙이 비어있다 => 다 섞어도 K보다 안 매운거
        else:
            return -1
