# 생성자가 여러 개인 경우는 뭐고
# 구글링

import sys
input = sys.stdin.readline

# 입력
n = int(input())

for i in range(n):
    # 분해합 공식
    digit_sum = i + sum(map(int, str(i)))
    # 생성자일 경우
    if digit_sum == n:
        print(i)
        break
else:
    print(0)