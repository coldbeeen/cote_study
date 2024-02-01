n = int(input())

garden = [list(map(int, input().split())) for i in range(n)]

def plant_in_garden(x_list, y_list):  # 매개변수로 들어온 위치들에 꽃을 심음
    graph = [[False for j in range(n)] for i in range(n)]  # 꽃을 심은 위치를 표시하기 위한 그래프
    sum_of_cost = 0
    for x, y in zip(x_list, y_list):
        if is_valid_position(x, y, graph):  # 심을 수 있는지 검사
            graph[x-1][y] = graph[x][y] = graph[x+1][y] = graph[x][y+1] = graph[x][y-1] = True  # 심었다라는 표시를 그래프에 True로 표현
            sum_of_cost += garden[x-1][y] + garden[x][y] + garden[x+1][y] + garden[x][y+1] + garden[x][y-1]  # 해당 위치의 비용 누적
        else:  # 심을 수 없다면 -1
            return -1
    return sum_of_cost  # 최종적으로 모두 심었다면 총 비용 리턴

def is_valid_position(x, y, graph):
    if graph[x-1][y] or graph[x][y] or graph[x+1][y] or graph[x][y+1] or graph[x][y-1]:  # 하나라도 True라면 (자리를 차지하고 있다면)
            return False
    return True

costs = []  # 모든 경우의 수의 비용을 담을 리스트

# 첫번째 꽃의 위치
for i1 in range(1, n-1):
    for j1 in range(1, n-1):

        # 두번째 꽃
        for i2 in range(1, n - 1):
            for j2 in range(1, n - 1):

                # 세번째 꽃
                for i3 in range(1, n - 1):
                    for j3 in range(1, n - 1):

                        x, y = (i1, i2, i3), (j1, j2, j3)  # 모든 위치를 담아
                        cost = plant_in_garden(x, y)  # 함수에 인자로 전달
                        if cost != -1:  # 총 비용이 유효하게 계산되었다면 누적
                            costs.append(cost)

print(min(costs))