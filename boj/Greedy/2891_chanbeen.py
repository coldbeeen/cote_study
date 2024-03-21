#리스트를 -1, 0, 1로 관리해주는 아이디어를 구글링해서 풀었음
# -1 : 고장, 0 : 출전 가능, 1 : 여유분 보유
#기존 방법은 예시가 다 돌아갔으나, 추가적인 반례가 생각나지 않았음

import sys
from collections import Counter

input = sys.stdin.readline

N, S, R = map(int, input().split())

broke_num = list(map(int, input().split()))

more_num = list(map(int, input().split()))

kayak = [0] * N #카약의 상태를 관리하는 리스트 생성

for i in broke_num: #부서진 보트 표시
    kayak[i - 1] = -1

for i in more_num:
    kayak[i - 1] += 1 #부서진 팀은 0, 안 부서진 팀은 1이 된다

print(kayak)

for i in range(N):
    if kayak[i] == 1: #안 부서졌고, 여유분이 있을 때
        if i - 1 >= 0 and kayak[i - 1] == -1: #이전 팀이 부서졌다면
            kayak[i - 1] += 1
            kayak[i] -= 1
            continue
        elif i + 1 < N and kayak[i + 1] == -1: #다음 팀이 부서졌다면
            kayak[i + 1] += 1
            kayak[i] -= 1
            continue
#for + list or tuple자료형 in = O(n^2)

print(kayak)

cnt = Counter(kayak)

print(cnt[-1]) #-1 : 부서졌는데 빌리지도 못하여 참가를 못하는 팀의 개수