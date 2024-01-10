n = int(input())
image = [list(map(int, input())) for i in range(n)]

def recursive(size, x, y):

    if size == 1:  # size가 한 칸까지 줄어 들면 해당 칸의 숫자 반환
        if image[x][y] == 0:
            return '0'
        else:
            return '1'

    half_size = size // 2  # sie를 절반으로 나누어 네 영역 검사할 것임
    # lt: left top, rb: right bottom
    lt = recursive(half_size, x, y)  # 왼쪽 위
    rt = recursive(half_size, x, y+half_size)  # 오른쪽 위
    lb = recursive(half_size, x+half_size, y)  # 왼쪽 아래
    rb = recursive(half_size, x+half_size, y+half_size)  # 오른쪽 아래

    if lt == rt == lb == rb == '1':  # 모든 영역이 1인 경우 1 반환
        return '1'
    if lt == rt == lb == rb == '0':  # 모든 영역이 0인 경우 0 반환
        return '0'

    # 모든 영역이 같지 않은 경우 각 영역의 반환 값을 활용하여 괄호에 넣기
    tmp = '(' + lt + rt + lb + rb + ')'  # 재귀를 통해 결과값이 점차 완성 됨
    return tmp

result = recursive(n, 0, 0)  # 재귀 함수: n 크기, (0,0) 위치부터 시작
print(result)