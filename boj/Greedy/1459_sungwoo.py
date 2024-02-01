import sys
input = sys.stdin.readline

x, y, w, s = map(int, input().split())

if w > s: # 대각선이 직선보다 이득이면 2
    diagonal = 2
elif w * 2 > s: # 대각선으로 가는게 이득이면 두 번 가는 것보다 이득이면 1
    diagonal = 1
else:  # 대각선이 손해면 0
    diagonal = 0 

result = 0

if diagonal == 2:
    result += min(x, y) * s  # 대각선 먼저 해치우기

    left = abs(x - y)  # 남은 거리
    result += (left // 2) * (s * 2)  # 2의 배수만큼을 대각선으로
    result += (left % 2) * w  # 남은 한 칸은 직선으로

elif diagonal == 1:
    result += min(x, y) * s  # 대각선 해치우고
    result += abs(x - y) * w  # 남은 거리 직선으로

else:
    result += w * (x + y)  # 무지성 직선


print(result)