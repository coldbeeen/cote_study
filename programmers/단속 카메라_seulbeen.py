# 백준의 회의실 같은 문제인듯
def solution(routes):
    answer = 1
    routes = sorted(routes, key=lambda x: x[1])
    # 차량의 진출 지점을 기준으로 정렬
    print(routes)

    camera = routes[0][1]  # 초기 카메라 설치 지점은 가장 일찍 나오는 차의 진출 지점

    for i in range(1, len(routes)):

        if camera < routes[i][0]:  # 카메라의 위치가 차량의 진입 지점보다 빠를 때
            # 카메라의 위치를 차량의 진출지점으로 놓고 카메라의 개수 +1
            camera = routes[i][1]
            answer += 1
        # 그렇지 않을때는 기존 카메라의 지점으로도 현재 차량을 만날 수 있으므로 pass

    return answer
