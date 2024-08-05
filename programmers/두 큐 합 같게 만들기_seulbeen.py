from collections import deque


def solution(queue1, queue2):
    answer = 0
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    q1_len = len(queue1)
    q2_len = len(queue2)
    if (q1_sum + q2_sum) % 2 != 0:
        return -1
    q1 = deque(queue1)
    q2 = deque(queue2)

    while True:
        # if len(q1)==0 or len(q2)==0:
        #    return -1
        # if q1_sum==0 or q2_sum ==0:
        #     return -1
        if answer == q1_len * 3:
            return -1
        if q1_sum > q2_sum:
            tmp = q1.popleft()
            q2.append(tmp)
            q1_sum -= tmp
            q2_sum += tmp

        elif q1_sum < q2_sum:
            tmp = q2.popleft()
            q1.append(tmp)
            q1_sum += tmp
            q2_sum -= tmp
        else:
            break
        answer += 1


    # 내 생각에는 q1_len * 2일때까지만 보는게 충분하다 생각했는데 맨 밑에 반례보고 걍 3으로 늘렸더니 되네
    # 이유는 도저히 모르겠음 너무 어렵다 ㅠㅠ

    # 11 15

    # 1 151
    # 0 1511

    # 111 5
    # 1115 0
    # 115 1
    # 15 11
    # 5 111
    # 0 1115
    # 1 115
    # 11 15

    # 111 5
    # 11 51
    # 115 1
    # 15 11

    # 1111 1171

    # 11111 171
    # 111111 71
    # 1111117 1
    # 111117 11
    # 11117 111
    # 1117 1111
    # 117 11111
    # 17 111111
    # 7 1111111

    # 71 111111
    # 711 11111
    # 7111 1111
    # 71111 111
    # 711111 11
    # 7111111 1

    return answer
