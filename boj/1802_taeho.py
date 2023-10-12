import sys
input = sys.stdin.readline


# 접을 수 있다면 True를 반환하는 재귀함수

def check(val): 
    if len(val) <= 1:
        return True
    
    mid = len(val)//2 # 중앙 인덱스
    left = val[:mid] # 분할
    
    # 맞은편 인덱스랑 달라야 함(out 반대는 in)
    for i in range(mid):
        if val[i] == val[-i-1]:
            return False # 같은 경우 못접음
        
    return check(left)

    
T = int(input())

for _ in range(T):
    val = input().rstrip()
    if check(val):
        print('YES')
    else:
        print('NO')