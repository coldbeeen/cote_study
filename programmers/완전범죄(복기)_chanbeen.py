#약 31분소요

def solution(info, n, m):
    dp = [[False] * m for _ in range(n)]
    
    dp[0][0] = True #아직 아무것도 안 훔침
    
    for aVal, bVal in info:
        next_dp = [[False] * m for _ in range(n)] #현재 물건 훔치는 시나리오 진행후 dp에 덮어씌우기
        
        for i in range(n):
            for j in range(m):
                if dp[i][j]: #이전 시나리오가 존재할 때만
                    if i + aVal < n: #A 검거 x
                        next_dp[i + aVal][j] = True
                    if j + bVal < m: #B 검거 x
                        next_dp[i][j + bVal] = True
            
        dp = next_dp
    
    answer = 1e9
    
    for i in range(n):
        for j in range(m):
            if dp[i][j]:
                answer = min(answer, i) #A도둑의 흔적 최소화
    
    return answer if answer != 1e9 else -1

#2^40은 시간 초과. 완전 탐색 불가능
#2차원 dp 활용
#행 : A가 훔쳤을 때 누적 흔적
#열 : B가 훔쳤을 때 누적 흔적
#next_dp를 기존 dp에 계속 갱신하며 마지막 물건까지 진행

#이 문제는 구글링 당시 신선한 충격을 받아서 복기 시에도 기억이 잘 났다