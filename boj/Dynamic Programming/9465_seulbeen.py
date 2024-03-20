import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n=int(input())
    dp=[list(map(int,input().split()))+ [0,0] for _ in range(2)] # 인덱스 에러 해결하기위해 0 패딩

    for i in range(1,n):
        dp[0][i]+=max(dp[1][i-1],dp[1][i-2])
        dp[1][i]+=max(dp[0][i-1],dp[0][i-2])
    
    print(max(dp[0][n-1],dp[1][n-1]))
"""
50 10 100 20 40
30 50 70 10 60

인접 스티커를 뗄 수 없다는 것을 고려하였을 때
각 위치에서의 최적해 = 대각선의 스티커를 떼고 자신의 것을 떼거나, 대각선 옆자리 스티커를 떼고 자신의 스티커를 떼는 경우


-------------------------------
사실 원래 dp배열이랑 arr배열 두개 선언하고, 백준에 제출하면서 '어 이러면 배열 하나만 써도 되겠네?'한건데 이게 웬걸? 오히려 하나만 쓴게 맞고 두개쓴건 틀려버림
이유를 모르겠음

import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n=int(input())
    arr=[list(map(int,input().split()))for _ in range(2)]
    dp=[[0 for _ in range(n)] for _ in range(2)]
    dp[0][0]=arr[0][0]
    dp[1][0]=arr[1][0]
    
    for i in range(1,n):
        dp[0][i]=max(dp[1][i-1],dp[1][i-2])+arr[0][i]
        dp[1][i]=max(dp[0][i-1],dp[0][i-2])+arr[1][i]
    print(max(dp[0][-1],dp[1][-1]))


"""