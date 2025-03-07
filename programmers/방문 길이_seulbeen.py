#50분
#처음에 이중 리스트로 실제 좌표를 구현했는데 딱히 그럴필요는 없었음
#a에서 b로 가는 길이 있었다고 하면, a->b를 다시 정확히 가는 경우와, b->a로 돌아오는 경우에 겹치는 길임
# 커맨드에 따라 a좌표에서 b좌표로 이동할때, (a,b),(b,a)를 모두 경로에 추가하고, 나중에 2로 나눠주면됨
# 이유는 나중에 b->a로 올때는 이미 겹치는 길이었으니 추가가 따로 되지 않을거라서
def solution(dirs):
    case = set()
    coord = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    cx, cy = 0, 0
    
    for d in dirs:
        dx = cx + coord[d][0]
        dy = cy + coord[d][1]
        if -5 <= dx <= 5 and -5 <= dy <= 5:
            # 현재 좌표와 이동 후 좌표를 case에 담음
            case.add((cx, cy, dx, dy))
            case.add((dx, dy, cx, cy))
            #현재 좌표 갱신
            cx = dx
            cy = dy

    return len(case) // 2
