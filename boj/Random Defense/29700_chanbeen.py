#약 20분 소요

N, M, K = map(int, input().split())

seats = [list(map(int, input().rstrip())) for _ in range(N)]

cnt = 0

for i in range(N):
    if M < K: #동아리원 수가 가로 좌석 수보다 크면 계산 스킵
        continue

    value = 0

    for j in range(K): #초기값 설정
        value += seats[i][j]
    
    if not value: #K개 모두 0
        cnt += 1

    idx = 0 #슬라이딩 윈도우 왼쪽 인덱스
    
    for j in range(K, M): #슬라이딩 윈도우 오른쪽 인덱스
        value -= seats[i][idx]
        value += seats[i][j]

        if not value:
            cnt += 1

        idx += 1

print(cnt) 

#가로로 0이 연속되는 개수가 K개 이상인 경우가 있는지 체크 -> 슬라이딩 윈도우