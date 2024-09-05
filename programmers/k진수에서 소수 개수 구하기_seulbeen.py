from collections import deque


def jinsoo(n, k):
    result = ""
    tmp = n
    while tmp != 0:
        r = tmp % k
        tmp //= k
        result += str(r)
    result = result[::-1]
    return result


def solution(n, k):
    answer = -1
    tmp = n
    result = jinsoo(n, k)
    result = result.split("0")

    cnt = 0
    for r in result:
        if len(r) == 0 or int(r) < 2:  # 비어있거나, 0,1(소수가 아님)면 continue
            continue
        prime = True
        number = int(r)

        for i in range(
            2, int(number**0.5) + 1
        ):  # 소수 판별(해당 숫자의 제곱근까지만 탐색하면 됨)
            if number % i == 0:
                prime = False
                break
        if prime:
            cnt += 1

    return cnt
