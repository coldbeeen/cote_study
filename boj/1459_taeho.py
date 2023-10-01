import sys
input = sys.stdin.readline

x, y, w, s = map(int, input().split())

#직선으로만 이동
case1 = (x + y) * w

#대각선으로만 이동
case2 = max(x, y) * s if (x + y) % 2 == 0 else (max(x, y) - 1) * s + w 

#혼합해서 하는 경우 == 대각이 이득인데 직선도 써야할 경우
#먼저 대각으로 다 이동하고
#남은 거리는 직선으로 이동
case3 = min(x, y) * s + abs(x - y) * w                                 


print(min(case1, min(case2, case3)))