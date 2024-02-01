import sys
input = sys.stdin.readline

caseNum = int(input())

for _ in range(caseNum):
    result = 0

    day = int(input())
    priceList = list(map(int, input().split()))

    M = priceList[-1]  # 맨 뒤 값을 최댓값으로 설정, 왜? 거꾸로 접근할 것임
    buySum, buyCnt = 0, 0  # 구매할 주식의 가격, 수를 설정
    for i in reversed(priceList[:-1]):  # 거꾸로 드가자~
        if i > M:  # 최댓값 갱신 조건
            result += M * buyCnt - buySum  # 지나간 구간의 이익 결산

            M, buySum, buyCnt = i, 0, 0  # 최댓값, 구매 주식 정보 초기화
            continue

        buySum += i
        buyCnt += 1

    result += M * buyCnt - buySum  # for문 이후 지나간 구간의 최종 이익 결산
    print(result)

''' 아래 입력 예시들을 끄적이면서 거꾸로 접근해야겠다는 아이디어가 떠오름
1 2 3 9 1 4 5 1 2 
1 2 3 5 4 100
1 2 8 1 9
9 10 1
앞에서 시작하게 되면 O(n)이 불가능한 것 같음.
사다가 파는 구간을 나눠야 하는데 앞에서부터 보게 되면 어디가 최댓값인지 알 수가 없어서 구간을 나누기 어려움. (2번 예시)
결국 파는 거는 각 구간별 마지막에 팔게 되니 마지막 값을 기준으로 거꾸로 순회하면서
더 큰 값이 나왔을 때 새로운 구간을 나눠주면 됨
'''