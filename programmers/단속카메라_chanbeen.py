def solution(routes):
    answer = 1
    
    routes = sorted(routes, key = lambda x: (x[1]))
    
    out = routes[0][1]
    
    for i in range(1, len(routes)):
        if routes[i][0] <= out <= routes[i][1]:
            continue
        else:
            answer += 1
            
            out = routes[i][1]
        
        print(answer)
    
    return answer

# 진출 시점 기준으로 정렬
# 최초 진출 시점을 변수로 저장
# 다음 route의 진입과 진출 시점 사이에 이전 route의 진출 시점이 위치한다면 단속 카메라 추가 설치 필요 x
# 만약 그렇지 않다면 추가 카메라 설치, 진출 시점 업데이트