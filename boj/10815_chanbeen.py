import sys

input = sys.stdin.readline

N = int(input())

SG = sorted(list(map(int, input().split())))#미리 정렬

M = int(input())

card = list(map(int, input().split()))
#일반 리스트로 하면 시간 초과, 이진 탐색 사용
for c in card:
    low, high = 0, N-1
    flag = 0
    
    while low <= high:
        mid = (low + high) // 2 #비교할 인덱스를 고정
        
        if SG[mid] > c: 
            high = mid - 1 #크면 범위를 mid 왼쪽으로 변경
        elif SG[mid] < c :
            low = mid + 1 #작으면 범위를 mid 오른쪽으로 변경
        else:
            flag = 1
            break
    
    print(1 if flag else 0, end=' ')