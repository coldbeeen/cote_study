import sys

N = int(sys.stdin.readline())

dp = [[0 for _ in range(3)] for _ in range(N + 1)]
rgb = [[0 for _ in range(3)]]

for _ in range(N):
    rgb.append(list(map(int, input().split())))
            
for n in range(1, N + 1):
    for i in range(3):
        dp[n][i] = min(dp[n-1][(i+1) % 3], dp[n-1][(i+2) % 3]) + rgb[n][i]

print(min(dp[N]))

"""
문제:

Nx3의 이중배열을 입력받는다. N번째에서 선택할 수 있는 것은 N-1번째 선택한 것과 같은 열에 있으면 안된다.
이때 N번째의 최솟값 구하기.
___________________________________________________________________________________________________
풀이:

dp배열과 rgb 배열을 먼저 초기화 해주었다. dp배열은 0번행이 0이 3개 채워지게 하여 인덱스 조회가 안되는 것을 해결하였다.
rgb배열도 직관에 맞게 1-3 인덱스를 쓰고 싶었는데 배열 입력받을 때 앞에를 0으로 비우면서 반복적으로 3개씩 받는 것에 어려움이 있어
0-2인덱스를 사용하였다.

로직은 단순하다.
dp[n][1]는 dp[n-1][0]과 dp[n-1][1] 중에서 더 작은 값과 현재 값을 더해주고 이걸 모든 rgb에 대해 반복해준다.
그러면 마지막 N번째에서 최소만 찾아주면 해결 가능하다.

이때 i번째가 달라짐에 따라 조건문을 일일이 쓰기보다 % 연산자를 활용해 한번에 처리해주었다.
"""