import sys

input = sys.stdin.readline

N, L = map(int, input().split())

pool = sorted([list(map(int, input().split())) for i in range(N)], key = lambda x : x[0])

cnt = 0

for i in range(len(pool)):
    length = pool[i][1] - pool[i][0]
    
    if i == len(pool) -1:
        cnt += (length-1) // L + 1 #마지막 위치 인덱스
        break
        
    if length % L != 0:
        rest = L - (length % L) #남은 널빤지의 길이
        
        new = pool[i][1] + rest #만큼 더 가보고
        
        if pool[i+1][0] <= new: #다음꺼를 겹칠 수 있다면 갱신
            pool[i+1][0] = new
            
        cnt += length // L + 1
    else:
        cnt += length // L #딱 나눠 떨어지면 +1 안 해줘도 됨

print(cnt)