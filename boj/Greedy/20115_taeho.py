# 가장 많은 양에 그 다음으로 많은 양 추가
# ED라는 리스트 정렬해서 절반 넣어줌

import sys
input = sys.stdin.readline

N = int(input())

ED = list(map(int, input().split()))

ED.sort(reverse=True)

sum = ED[0]

for i in range(1, N):
    sum += ED[i]/2

print('%g'%sum) #소수점 없애서 출력하는 코드