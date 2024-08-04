def solution(m, n, puddles):
    answer = 0
    
    ways = [[0] * (m + 1) for _ in range(n + 1)]
        
    ways[1][1] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            
            if [j, i] in puddles:
                ways[i][j] = 0
            else:
                ways[i][j] = (ways[i - 1][j] + ways[i][j - 1]) 
    
    answer = ways[-1][-1] % 1000000007
    
    return answer

#puddles 조건문에서 세로 좌표 먼저 오는 것에 유의
#배열 초기화 시 1로 초기화하면 사이드에 웅덩이가 존재할 때 계산이 틀리는 케이스가 있으므로 유의