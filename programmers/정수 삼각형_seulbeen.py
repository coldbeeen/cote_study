def solution(triangle):
    
    for i in range(1, len(triangle)): #루트층 제외 1번째 층부터 돌아감(루트에 있는건 항상 거쳐가야됨)

        for j in range(len(triangle[i])): #한 층의 원소들을 돌면서

            if j == 0:  # 왼쪽 끝 원소면 이전층의 첫번째 원소를 더해줌
                triangle[i][j] += triangle[i - 1][0]

            elif j == len(triangle[i]) - 1:  # 오른쪽 끝 원소면 이전층의 오른쪽 끝 원소를 더해줌
                triangle[i][j] += triangle[i - 1][j - 1]
            
            else: # 중간 원소면 이전층의 왼쪽, 오른쪽 원소중 큰 값을 더해줌
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

    # 제일 아래층의 원소들 중 max값 반환
    return max(triangle[-1])
