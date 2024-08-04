def solution(routes):

    answer = 1

    # 진출 지점을 기준으로 정렬함. 진출 지점(end)을 기준으로 단속 카메라 개수를 결정하기 때문임
    routes.sort(key=lambda x: x[1])

    # 초기값(end) 설정한 뒤 routes 순회
    end = routes[0][1]
    for route in routes[1:]:

        # 해당 route의 진입 지점이 end(기준값)보다 크다면 단속 카메라 추가 및 end(기준값) 갱신
        if route[0] > end:
            answer += 1
            end = route[1]

    return answer