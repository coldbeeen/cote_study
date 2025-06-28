#약 49분 소요

import sys

input = sys.stdin.readline

def check(height):
    if light[0] > height: #첫 가로등
        return False
    
    for i in range(1, len(light)):
        if light[i] - light[i - 1] > 2 * height: #각 가로등은 가로등 간 거리를 절반씩 비춰줌
            return False
    
    if N - light[-1] > height: #마지막 가로등
        return False
    
    return True

N = int(input())
M = int(input())

light = list(map(int, input().split()))

left = 1
right = N

answer = N

while left <= right:
    mid = (left + right) // 2

    if check(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)

#x 위치는 오름차순으로 전달 -> 이분 탐색으로 시도
#굴다리 길이보다 높이는 안 높아도 되니, 1부터 N으로 범위 설정하여 이분 탐색
#N log N으로 해결하기 위해, 체크하는 조건문은 O(N)으로 작성
#처음/중간/마지막 가로등별 조건문 설정 필요
#중간 가로등 끼리는 서로 간 존재하는 여백을 절반씩 비춤, 따라서 거리가 2일 때 높이가 1이어도 길을 다 밝힐 수 있음