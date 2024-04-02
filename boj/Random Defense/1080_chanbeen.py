import sys

input = sys.stdin.readline

def reverse_array(x, y):
    for i in range(3):
        for j in range(3):
            if A[x + i][y + j] == '0':
                A[x + i][y + j] = '1'
            else : 
                A[x + i][y + j] = '0'

def check():
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return False
    return True

N, M = map(int, input().split())

A = [list(input().rstrip()) for _ in range(N)]
B = [list(input().rstrip()) for _ in range(N)]

cnt = 0

if N >= 3 and M >= 3: #3x3 필터 연산이 가능한 사이즈일 때
    for i in range(N - 2):
        for j in range(M - 2): #3x3 필터이므로 범위 설정 중요
            if A[i][j] != B[i][j]:
                reverse_array(i, j)
                cnt += 1

print(cnt if check() else -1)

#완전 탐색 문제같은데?
#컨볼루션 필터처럼 3x3 필터 씌워서 전부 뒤집는 방식
#모든 부분행렬을 돌면서 다른 요소가 존재하는지 확인해봐야 함 : 완전 탐색
#NxM만큼 돌면서 다른 요소 있을 때마다 3x3 필터만큼 뒤집는 것이 최적의 방법

#N과 M 중 하나가 3보다 작을 때 무조건 -1을 반환하는 게 안 됨
#입력 당시부터 A, B가 같다면 0을 반환해야하는 것에 유의

#1%에서 틀렸다..? -> 반복문 돌고난 후 A, B가 같은지 check를 안 해줬었음
#check 함수를 만들어서 A와 B가 같다면 cnt, 아니면 -1 