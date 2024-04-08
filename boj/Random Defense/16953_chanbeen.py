import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

A, B = map(int, input().split())

result = {}

def calculate(num, cnt):
    if num >= B:
        result[num] = cnt
        
        return
    
    calculate(num * 2, cnt + 1)
    calculate(num * 10 + 1, cnt + 1)

calculate(A, 1)

print(result[B] if B in result.keys() else -1)

#DP 
#가능한 연산들
#1. 2를 곱한다
#2. 10을 곱하고 1을 더해준다
# -> DP로 풀었더니 메모리 초과, 엄청 큰 예시가 있나보다
# 찾아보니, 길이가 1억정도되면 400MB 정도 한다고 한다

# 1차원 배열도 생성 안 하고 푸는 방법..?
# 딕셔너리를 활용한 재귀문으로 시도 -> 정답 처리됨