# 서류 오름차순
# 면접 결과 기준으로, 서류 심사 내 윗 등수보다 등수가 높아야 함
# 서류 1등은 어차피 뽑히니까, 면접 2등부터 보면 됨
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())

    a = [] #배열

    for j in range(n):
        x,y = map(int(input().split()))
        a.append([x,y])

    a.sort()

    print(a)
    '''

    L = a[0][1]
    index = 1

    for j in range(1,n):
        if a[j][i] < L:
            L = a[j][1]
            index += 1
    print(index)
    '''



"""
T = int(input())

for _ in range(T):
    N = int(input())
    rank = [list(map(int, input().split())) for _ in range(N)]
    rank_asc = sorted(rank)
    top = 0
    result = 1
    
    for i in range(1, len(rank_asc)):
        if rank_asc[i][1] < rank_asc[top][1]:
            top = i
            result += 1
    
    print(result)
"""