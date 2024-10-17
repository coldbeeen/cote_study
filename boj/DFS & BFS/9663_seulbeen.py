"""
1차원 배열로 풀 수 있다!
배열의 인덱스 : 행
각 인덱스당 숫자 : 해당 열에 퀸이 있다.
[1,2,2] -> 0번째 행 1번째 열에 퀸, 1번쨰 행 2번쨰 열에 퀸, 2번쨰 행 2번쨰 열 퀸
"""
"""
불능 조건
1. 같은 행에 퀸을 놓을 수 없다 -> 애초에 못놓게 설정 (1차원 배열이니까)
2. 같은 열에 퀸을 놓을 수 없다 -> 배열에 같은 숫자(열)가 있으면 안됨
3. 대각선에 퀸을 놓을 수 없다 -> 행번호간의 차이 == 해당 행 성분들끼리 차이 이면 대각선인 것
"""

import sys
input=sys.stdin.readline
n=int(input())
result=0
chess=[0]*n
visit=[False]*n
def valid(idx):
    for i in range(idx):
        if chess[idx]==chess[i] or idx-i == abs(chess[idx]-chess[i]):
            return False
    return True

def backtracking(idx):
    global result
    #종료조건
    if idx==n:
        result+=1
        return

    for i in range(n):

        if visit[idx]==False:
            chess[idx]=i

            if valid(idx):
                visit[idx]=True
                backtracking(idx+1)
                visit[idx]=False
backtracking(0)
print(result)