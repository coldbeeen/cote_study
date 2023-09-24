import sys

input = sys.stdin.readline

X, Y, W, S = map(int, input().split())

short, long = min(X, Y), max(X, Y) #가로 세로 중 짧은 쪽과 긴 쪽 지정
time = 0
#전략 : 정사각형 넓이만큼 일단 직진하고, 그 다음에는 경우에 맞게 해결한다

if 2 * W < S: #대각선보다 직진이 더 빠르다면
    time += short * 2 * W #정사각형 거리 전진
    long -= short
    time += long * W
else: #대각선이 직진보다 빠르다면
    time += short * S #정사각형 거리 전진
    long -= short
    if W < S: #남은 거리에서, 직진이 더 빠르다면
        time += long * W
    else: #남은 거리에서, 대각선이 더 빠르다면 지그재그로도 갈 수 있음
        if long % 2 == 0: #남은 거리가 짝수면 지그재그로 도착할 수 있음
            time += long * S
        else: #남은 거리가 홀수면 지그재그로 도착 못 함
            time += long // 2 * 2 * S
            time += W #직진 한 번은 무조건 있어야 됨

print(time)