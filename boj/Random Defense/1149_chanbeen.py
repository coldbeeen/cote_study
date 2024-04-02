import sys

input = sys.stdin.readline

N = int(input())

RGB = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N): #0번째 인덱스는 계산 필요 x
    RGB[i][0] += min(RGB[i - 1][1], RGB[i - 1][2])
    RGB[i][1] += min(RGB[i - 1][0], RGB[i - 1][2])
    RGB[i][2] += min(RGB[i - 1][0], RGB[i - 1][1])
    
print(min(RGB[-1]))

#시간 0.5초에 추가 시간 없다길래 DP로 풀었음
#2중 반복문으로 넘어가면 시간 초과 뜰수도 있겠다고 생각함

#본인의 인덱스를 제외하고 페인트를 선택할 수 있으므로 각 row당 R, G, B가 선택될 경우를 3열로 계산
#예시 : i행 0번째 열은 R이 선택될 경우이므로 i-1행 1열(G)와 i-1행 2열(B) 중 더 작은 값을 더해주면 됨