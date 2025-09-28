# 볼 모으기
# 30분가량
"""
붙어있는 볼뭉텅이는 한번에 건너뛸 수 있음
strip함수를 이용하여 뭉텅이를 통째로 제거하고, 남은 공들만 옮기면 됨
빨강/파랑 색 뭉텅이를 좌측으로 옮기냐, 우측으오 옮기냐 각각 4번을 수행하면 될듯    
"""
import sys
input=sys.stdin.readline
N = int(input().rstrip())
balls = str(sys.stdin.readline().strip())
cnts = []
# 빨강색을 우측으로 모으기 위해 우측 뭉텅이 제거
red_right = balls.rstrip('R')
cnts.append(red_right.count('R'))
# 파랑생을 우측으로 모으기 위해 우측 뭉텅이 제거
blue_right = balls.rstrip('B')
cnts.append(blue_right.count('B'))
# 빨강색을 좌측으로 모으기 위해 좌측 뭉텅이 제거
red_left = balls.lstrip('R')
cnts.append(red_left.count('R'))
# 파랑색을 좌측으로 모으기 위해 좌측 뭉텅이 제거
blue_left = balls.lstrip('B')
cnts.append(blue_left.count('B'))

result=min(cnts)
print(result)
