import sys

input = sys.stdin.readline

N = int(input())

candy = [[s for s in input().rstrip()] for _ in range(N)] #각 문자를 2차원 리스트로 입력받기

def maxnum(array):
    max_row, max_char = 0, 0
    
    for i in range(N): #가로 세기
        row = array[i][0] #각 행의 처음 값으로 초기화
        cnt = 0
        for j in range(N):
            if array[i][j] == row: #같은 문자가 연속 될 때 계속 카운트
                cnt += 1
            else: #다른 문자가 등장했을 때
                cnt = 1 #개수를 1로 초기화
                row = array[i][j] #비교 문자를 새로운 문자로 초기화
                
            if max_row < cnt: #최대 연속 등장 개수 저장
                max_row = cnt
                    
    for i in range(N): #세로 세기
        char = array[0][i] #각 열의 처음 값으로 초기화, 이후는 가로 세기와 동일
        cnt = 0
        for j in range(N):
            if array[j][i] == char:
                cnt += 1
            else:
                cnt = 1
                char = array[j][i]
            
            if max_char < cnt:
                max_char = cnt
                    
    return max(max_row, max_char)

result = []

for i in range(N):
    for j in range(N):
        if j != N-1: #가로 스왑
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            result.append(maxnum(candy))
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j] 
        if i != N-1: #세로 스왑
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            result.append(maxnum(candy))
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            #스왑했다가 다시 돌려놔야됨
print(max(result))