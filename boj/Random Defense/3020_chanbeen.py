#90분 +@, 구글링

n, h = map(int, input().split())

down = [0] * (h + 1)  # 석순
up = [0] * (h + 1)  # 종유석

min_count = n  # 파괴해야 하는 장애물의 최소값
range_count = 0  # 최소값이 나타나는 구간의 수

for i in range(n):
    size = int(input())
    
    if i % 2 == 0: #석순
        down[size] += 1
    else: #종유석
        up[size] += 1

for i in range(h - 1, 0, -1): #누적합, 석순 또는 종유석은 자라는 방향이 고정되어 있으므로 누적합으로 구간별 충돌 개수 계산 가능
    down[i] += down[i + 1] 
    up[i] += up[i + 1]

for i in range(1, h + 1): #각 i는 개똥벌레가 통과하는 높이

    if min_count > (down[i] + up[h - i + 1]): #종유석은 거꾸로 자라므로 적절하게 인덱싱
        min_count = (down[i] + up[h - i + 1])
        range_count = 1
    elif min_count == (down[i] + up[h - i + 1]):
        range_count += 1

print(min_count, range_count)

#석순 기준, 아래에서 위로 자라므로 높이 5에 석순에서 부딪혔다면 높이 4에도 석순은 존재함
#따라서 h 높이에서 각 구간별 충돌 개수를 누적합으로 구할 수 있다