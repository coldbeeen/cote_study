import sys
from collections import deque

N = int(sys.stdin.readline())

stack = []
for i in range(N):
    L, H = map(int, input().split())
    
    stack.append((L, H))

# 높이를 기준으로 정렬
stack.sort(key=lambda x: x[1])

# top을 받아서 초기값으로 사용
top = stack.pop()
former_l, h = top[0], top[1]

# 초기에는 l과 r이 같은 값을 가짐
former_r = former_l

# 처음 넓이는 top의 기둥 넓이로 초기화
total = 1 * h

while stack:
    # 스택이 빌 때까지 top을 받음.
    # 해당 스택은 높이가 점점 작아지는 구성
    top = stack.pop()
    current_l, current_h = top[0], top[1]

    if former_l < current_l < former_r:
        # 만약 pop받은 l의 위치가 기존 l, r의 사이에 있다면 더 작은 높이를 가진 것이므로 넓이 계산에 고려하지 않아도 됨
        # l이 같은 경우는 없기에 등호는 고려x
        pass

    if current_l < former_l:
        # 현재의 l값이 이전 l값보다 작다면 width를 계산해 현재 높이와 곱해 넓이를 구하고 total에 더해준다
        width = former_l - current_l
        total += width * current_h

        # former_l을 최신화
        former_l = current_l
        
    if former_r < current_l:
        width = current_l - former_r
        total += width * current_h

        former_r = current_l

print(total)

"""
풀이:

임의의 순서로 입력받은 튜플의 리스트를 높이를 기준으로 정렬한다.
이후 스택 자료구조를 활용해 가장 높은 기둥부터 pop하고
l, r의 위치를 관리하면서 넓이를 구해준다.

이 때, 리턴받은 l값이 기존 l, r 사이에 있다면 해당 기둥의 높이는 기존보다 무조건 작거나 같으므로 넓이를 고려할 필요없이 pass하면 된다.
나머지의 경우는, 리턴받은 l값을 기존 l, r과 대소비교하여 위치를 찾고 넓이를 계산해주어 total에 더한다.
"""