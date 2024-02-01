# 조건1: 이동 횟수가 4번보다 적지 않다면, 이동 방법을 모두 한 번씩 사용
# 조건2: 이동 횟수가 4번보다 적은 경우(방문한 칸이 5개 미만)에는 이동 방법에 대한 제약 X

import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 세로 x 가로

result = 1

if n == 1:  # 이동 불가
    pass

elif n == 2:  # 세로 2칸 이동 불가
    result += min((m-1) // 2, 3)  # (모든 이동 방법 사용 조건, 이동 횟수 4회 미만은 무시 가능 조건으로) 최대 3칸 방문 가능
    
else:  # 세로 2칸 이동 가능

    # 모든 이동 방법 사용 조건을 위해, 먼저 오른쪽 한 칸씩 이동
    if m >= 3:
        result += 2
        if m >= 7:  # 모든 이동 방법 사용하는 조건
            result += 2  # 오른쪽 두 칸식 이동했고

            result += (m-7)  # 이제 남은 칸 한 칸씩 돌진!!

        else:  # 외엔 오른쪽 한칸만 더 전진 가능 (위 두 조건으로 인해)
            result += 1 if m >= 4 else 0

    else:
        result += m - 1


print(result)