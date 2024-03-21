import sys

input= sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    arr = [[]]
    arr.append([0] + list(map(int, input().split())))
    arr.append([0] + list(map(int, input().split())))
    # 스티커 별 점수 입력 (0행과 0번 컬럼은 편의상 0으로 비워둠)
    
    dp = [arr[1][1], arr[2][1]]  # 1열의 초기값
    max_past = max(0, 0)         # max_past에는 아래 반복문 기준 j-2 열의 dp 최대값을 저장. 처음은 0번 컬럼이므로 0
    for j in range(2, n + 1):
        tmp = max(dp)   # 임시로 현재 dp 배열의 최대값 저장

        # dp 배열은 이전 dp배열값과 다음 값의 합을 저장
        dp = [max(dp[1], max_past) + arr[1][j], max(dp[0], max_past) + arr[2][j]]
    
        max_past = tmp  # 임시 저장했던 것을 max_past로 넘겨줌
    print(max(dp))

