# 구글링

for _ in range(int(input())):
    n = int(input())
    data = list(map(int,input().split()))
    answer = 0 
    mx = data[-1]
    for i in range(n-2,-1,-1):
        if data[i] > mx: #오늘 가격이 mx라면 
            mx = data[i]
        else:
            answer += mx-data[i] #오늘 가격이 최대가 아니라면 최대-지금가격만큼 더한다 
    print(answer)

    '''
    질문 검색에서 볼 수 있듯, 리스트의 뒤부터 조회하면 시간 초과를 해결할 수 있다 

1. 최대값을 우선 data[-1]로 잡아두고 

2. 인덱스 i의 범위를 range(n-2,-1,-1)로 잡은 뒤에 

    1. data[i]가 최대값보다 크다면 최대값을 갱신하고 

    2. data[i]가 최대값보다 작다면 최대값에서 현재 가격을 뺀만큼을 답에 저장해준다 
    '''