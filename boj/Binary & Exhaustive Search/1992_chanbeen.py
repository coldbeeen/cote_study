#구글링
import sys

input = sys.stdin.readline

N = int(input())

quad = [list(map(int, input().rstrip())) for _ in range(N)]

def dnc(x, y, N): #분할정복이랑 백트래킹의 차이점은?
    point = quad[x][y]
    
    for i in range(x, x + N):
        for j in range(y, y + N): #구역 내 탐색
            if point != quad[i][j]: #같지 않은 요소가 보인다면
                point = -1
                break #더 쪼개주기 위해 중단
            
    if point == -1: #더 쪼개줘야 한다는 뜻
        print('(', end='') #더 쪼개기 전에 여는 괄호 출력해줘야 함
        
        N = N // 2
        
        dnc(x, y, N) #네 구역 중 왼쪽 위
        dnc(x, y + N, N) #오른쪽 위
        dnc(x + N, y, N) #왼쪽 아래
        dnc(x + N, y + N, N) #오른쪽 아래
        
        print(')', end='') #닫는 괄호 출력
    
    elif point == 1: #모든 요소가 1로 동일하였다는 뜻
        print(1, end='')
    else: #모든 요소가 0으로 동일하였다는 뜻
        print(0, end='')

dnc(0, 0, N) #맨 처음 좌표부터 분할 시작




#구글링 전 논리
# 1. 각 구역의 크기가 4가 될 때까지 구역을 4등분하면서 재귀 호출 (N을 계속 반띵)
# 2. 크기가 4가 되기 전이라도 구역 내 요소가 모두 같다면 그 요소 하나만 출력 (1 or 0)
# 3. 구역의 크기가 4가 되었지만 구역 내 요소가 모두 같지 않다면 구역 내의 값 모두 출력
# 4. 재귀 함수 호출 전에 '(' 출력, 재귀 함수 호출 후에 ')' 출력

#구글링 후 든 생각
# 4번만 맞았네 ㅋㅋ