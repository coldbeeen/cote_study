#90분 +@, 구글링

def solution(name):

	# 조이스틱 조작 횟수 
    answer = 0
    
    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1
    
    for i, char in enumerate(name):
    	# 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) -next)])
        
    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    
    return answer

#왼쪽 또는 오른쪽으로 쭉 진행하는 것이 최소인 줄 알았지만, 이미 지나온 인덱스를 다시 거쳐가는 것이 최소가 될 때가 있음
#모든 경우의 수를 봐야한다고 생각되어서, 완전 탐색을 고려하게 됨
#각 인덱스에서마다 왼쪽 오른쪽을 재귀문으로 호출하면 최대 2 ** 20이기 때문에 안 되겠다고 생각

#결국 좌우를 어떻게 최소 횟수로 이동하느냐가 중요했던 문제
#21번째 줄은 이전으로 돌아가도 못 떠올릴 듯