# 45분
# 생각해보니까 똥창(구석)에 쳐야하는 경우가 최소일수가 없음, 항상 그거보다 작은경우가 존재
# 입사각==반사각이니까 그냥 벽애 대칭시켜서 거리 구하면 되네
# 상하좌우 벽에 칠때의 거리 중 최소를 구하면 될거 같네
# 근데 x나 y 좌표가 같으면, 못 치는 벽이 존재
# 예외 케이스를 생각 안했음 : 걍 일자로 치면 되는경우(도착점과 벽 사이에 출발점 있는 경우)



def solution(m, n, startX, startY, balls):
    answer = []

    #거리 계산 함수
    def distance(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    #4방향 벽을 이용하는 경우 중 최소 계산
    def find_min(sx, sy, x, y):
        # 가로 m,세로 n
        # 왼쪽으로 치거나, 오른쪽으로 치거나, 상하벽중 출발점쪽에 가까운 벽

        #x좌표가 같으면, 좌우 벽에 반사 시키거나, 위아래 중 한벽에 일자로 치는 경우(벽을 맞기전에 공이 맞으면 안되니까)
        if sx == x:
            left = distance(-sx, sy, x, y)
            right = distance(2 * m - sx, sy, x, y)
            # 출발점이 위쪽일때 위쪽벽, 아래쪽일때 아래쪽 벽
            straight = (n - sy) + (n - y) if sy > y else sy + y
            return min([left, right, straight])
        #y좌표가 같으면 위 아래 벽에 각각 반사 시키거나, 좌우 중 한벽에 일자로 치는 경우
        if sy == y:
            up = distance(sx, 2 * n - sy, x, y)
            down = distance(sx, -sy, x, y)
            # 출발공이 오른쪽일때 오른쪽 벽, 왼쪽일때 왼쪽 벽
            straight = (m - sx) + (m - x) if sx > x else sx + x

            return min([up, down, straight])
        
        # 다 비교해봐야 되는경우
        left = distance(-sx, sy, x, y)
        right = distance(2 * m - sx, sy, x, y)
        up = distance(sx, 2 * n - sy, x, y)
        down = distance(sx, -sy, x, y)
        return min([left, right, up, down])

    for b in balls:
        #최소거리 구하고
        dis = find_min(startX, startY, b[0], b[1])
        #제곱해서 append
        answer.append(int(dis**2 + 0.5))

    return answer
