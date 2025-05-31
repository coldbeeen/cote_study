# 25분
import sys
sys.setrecursionlimit(100000)

def solution(n):
    answer = []

    def hanoi(N, start, tmp, target):

        # 탈출조건 : 1개짜리 탑(그냥 가장 작은 원반 하나) 을 옮길때, 아무런 제약 없이 옮기기 가능
        if N == 1:
            # start -> target으로 원반 하나 옮김
            # print((start,target))
            answer.append([start, target])
            return
        
        # 가장 밑에 있는 원반을 옮기기 위해, 그 위의 N-1개로 이루어진 탑을 tmp로 옮기는, 'N-1하노이' 수행
        hanoi(N - 1, start, target, tmp)
        
        # print((start,target))
        # start에 가장 큰 원반이 남아있고, N-1개의 탑은 tmp에 있음
        # start에 있던 가장 큰 원반을 target으로 옮김
        answer.append([start, target])

        # tmp에 있는 N-1개 탑을 타겟으로 옮기는 'N-1하노이'수행 . 재귀적으로 
        hanoi(N - 1, tmp, start, target)

    hanoi(n, 1, 2, 3)
    return answer
"""
n개로 이루어진 탑이 있음
n-1개의 탑을 tmp로 옮김
가장 밑에 있는 원반을 target으로 옮김
...
n-1개로 이루어진 탑이 tmp(start역할)에있음
n-2개의 탑을 start(tmp역할)로 옮김
가장 밑에 있는 원반을 target으로 옮김
...

"""
