#구글링

N = int(input())

cards = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(1, i + 1):
        if not dp[i]:
            dp[i] = dp[i - j] + cards[j] #비용 초기화, 이후 기존 비용으로 사용됨
        else:
            dp[i] = min(dp[i], dp[i - j] + cards[j]) #기존 비용 vs 경우의 수를 조합하여 만든 비용

print(dp[N])

#N 종류의 카드 사는데 필요한 최소 금액 -> DP
#동전 조합해서 특정 금액 만드는 문제와 유사?

#구글링
#0으로 dp를 초기화
#i 인덱스까지만 카드 종류를 사용해서, 더 적은 비용으로 i개의 카드 구매하는 경우 찾기
#i 인덱스를 N까지 확대하여, N개의 카드를 구매할 때 cards[N]이 저렴한지 or 다른 경우가 있는지 탐색

#DP 유형은 흐름을 타지 못 하면 정말 헤매게 되는 유형인 것 같다