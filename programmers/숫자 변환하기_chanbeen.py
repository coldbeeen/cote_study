#약 34분 소요

def solution(x, y, n):
    num = 1e9
    
    dp = [num] * (y + 1)
    
    dp[x] = 0
    
    for i in range(x + 1, y + 1):
        if dp[i - n] != num: #x에 n을 덧셈
            dp[i] = min(dp[i], dp[i - n] + 1)
        
        if dp[i // 2] != num and i % 2 == 0: #x에 2를 곱셈
            dp[i] = min(dp[i], dp[i // 2] + 1)
        
        if dp[i // 3] != num and i % 3 == 0: #x에 3을 곱셈
            dp[i] = min(dp[i], dp[i // 3] + 1)
    
    return dp[y] if dp[y] != 1e9 else -1 #초기값에서 갱신되지 않았다면 x에서 y로 도달 불가능

#dp 유형의 문제였던걸로 기억
#노션에 정리해둔 이코테를 참고했음
#계산 방식이 3가지 존재하므로, 3가지 중 각 조건에 부합할 경우 min 함수로 연산 횟수를 카운트하는 방식
#조건문에서 나머지가 0이 아니게 되면 dp[2]가 1e9가 아닐 때 두번째 조건문에서 dp[4]도 갱신되고 dp[5]도 갱신됨
#따라서 나머지에 대한 추가 필터링이 필요함