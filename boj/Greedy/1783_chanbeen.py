#입력 범위가 20억이니까, 반복문은 안 쓸 수 있으면 안 쓰는 게 좋겠다
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

cnt = 0

#나이트가 체스판 위에 현재 서있는 곳도 1칸으로 침
if N == 1 or M == 1: #가로 또는 세로가 1이면 나이트는 이동 불가
    cnt = 1
    
if 1 < M < 7:
    if N >= 3:
        if M < 5:
            cnt = M
        else :
            cnt = 4 #이동 방식을 한번씩 안 썼으므로 리미트가 걸림
    elif N == 2:
        if M % 2 == 0:
            cnt = M // 2
        else:
            cnt = M // 2 + 1 #M이 홀수면 나이트가 갈 수 있는 곳이 하나 추가됨
elif M >= 7:
    if N >= 3:
        cnt = (M - 2) 
        #처음에 4가지 방식 다 사용하면서 오른쪽으로 2칸을 2번 갔으므로 오른쪽으로 1칸씩만 갔을 때(M)보다 2칸 손해
    elif N == 2:
        cnt = 4 #이동 방식을 한번씩 안 썼으므로 리미트가 걸림

print(cnt)