# 이건 꼭 풀어야 해!
# 9분
# 사실 누적합을 활용하는 문제인 것을 몰랐다면 시간이 더 소요되었을 것 같다.

import sys

input = sys.stdin.readline

N, Q = map(int, input().split(" "))
#누적합 배열 선언
pre_sum = [0 for _ in range(N)]

#문제에서 제시한 수열을 비내림차순으로 정렬
a = sorted(list(map(int, input().split(" "))))


pre_sum[0] = a[0]
# pre_sum[i]= i번째 숫자까지의 누적합
for i in range(1, N):
    pre_sum[i] = pre_sum[i - 1] + a[i]

# 인덱스 관리 쉽게하려고 0추가 
# l부터 r까지의 합 = r까지의 누적합 - l-1까지의 누적합
pre_sum = [0] + pre_sum
for _ in range(Q):
    l, r = map(int, input().split(" "))
    result = pre_sum[r] - pre_sum[l - 1]
    print(result)
