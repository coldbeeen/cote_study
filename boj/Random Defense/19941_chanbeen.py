N, K = map(int, input().split())

ham = list(input())

cnt = 0

for i in range(len(ham)):
    if ham[i] == 'P':
        for j in range(i - K, i + K + 1): #좌 ~ 우 K씩 탐색
            if 0 <= j < len(ham) and ham[j] == 'H': #먹을 수 있는 햄버거 등장 시
                cnt += 1
                
                ham[j] = 'X' #먹었음 처리
                break

print(cnt)