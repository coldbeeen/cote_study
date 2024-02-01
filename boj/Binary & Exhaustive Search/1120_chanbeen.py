import sys

input = sys.stdin.readline

A, B = map(str, input().split())

result = len(B)

for i in range(len(B) - len(A) + 1):
    cnt = 0
    
    for j in range(len(A)):
        if A[j] != B[i+j]:
            cnt += 1
    
    if result > cnt:
        result = cnt
        
print(result)

#B문자열 안을 돌면서 A문자열의 문자와 안 겹치는 개수 탐색
#개수가 가장 적을 때, 결과 출력
#아무 문자나 추가하는 거는 B문자열과 같은 문자를 추가하면 되기 때문