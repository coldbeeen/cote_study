from collections import deque

def solution(queue1, queue2):

    # 큐 자료구조로 변경 (데크 활용)
    dq1, dq2 = deque(queue1), deque(queue2)

    answer = 0
    s1, s2 = sum(queue1), sum(queue2)

    # 큐의 길이의 3배 만큼 반복
    for i in range(len(queue1)*3):

        # 합이 더 큰 쪽의 큐에서 추출하여 더 작은 쪽의 큐에 삽입, 그리고 큐의 합 갱신
        if s1 > s2:
            e = dq1.popleft()
            dq2.append(e)
            s1, s2 = s1 - e, s2 + e
        elif s1 < s2:
            e = dq2.popleft()
            dq1.append(e)
            s1, s2 = s1 + e, s2 - e
        else:
            break

        answer += 1

    else:  # break를 만나지 못한 경우, 합을 갖게 만들지 못하는 것이므로 -1 리턴
        return -1

    return answer

# 참고 - 최대 순회 가능한 횟수에 대한 이해를 위해 아래 글을 참고하시기 바랍니다!
# https://tae-hui.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%91%90-%ED%81%90-%ED%95%A9-%EA%B0%99%EA%B2%8C-%EB%A7%8C%EB%93%A4%EA%B8%B0-Level2-2022-KAKAO-TECH-INTERNSHIP