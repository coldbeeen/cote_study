# 주몽
# 12분

import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
# 재료를 리스트로 받고 정렬
ing = sorted(list(map(int, input().split(" "))))

# 투 포인터 초기화
l, r = 0, len(ing) - 1
cnt = 0

while l < r:
    fir, sec = ing[l], ing[r]
    # 재료가 두가지 필요하므로 두번째 재료 혼자 M을 충족해 버리면 안됨
    if sec < M:
        # 두 재료합이 M 일때 OK
        if fir + sec == M:
            cnt += 1
            l += 1
            r -= 1
        # M보다 작으면 왼쪽포인터를 늘려서 합을 크게 만듦
        elif fir + sec < M:
            l += 1
        # M보다 크면 오른쪽포인터를 줄여서 합을 작게 만듦
        elif fir + sec > M:
            r -= 1
    else:
        r -= 1
print(cnt)
