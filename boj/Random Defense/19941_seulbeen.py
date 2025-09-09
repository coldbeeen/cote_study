# 햄버거 분배
# 39분
"""
왼쪽부터 탐색하는 케이스랑 오른쪽부터 탐색하는 케이스를 나눠서 하려했음
생각해보니 그럴필요가 없었다.
1. 그냥 모두에게 왼쪽 혹은 오른쪽부터 탐지하는 동일한 규칙을 적용(어차피 뒤집으면 똑같을 것)
2. 나같은 경우에는 왼쪽을 설정하였고, 해당 인덱스에서 '왼쪽부터 오른쪽'으로 훑으면 됨 
 => (index-k ~ index+k) 범위를 탐색하면서 가능한 먼 햄버거를 먹게됨
"""

import sys
input=sys.stdin.readline

n,k=map(int,input().split())

table=list(input().rstrip())
# print(table)

cnt=0

def eat_h(cur):
    global cnt
    # 왼쪽으로 k떨어진 곳부터 오른쪽으로 k 떨어진 곳까지 탐색
    for idx in range(cur-k,cur+k+1):
        #햄버거 발견시 먹고 종료
        if 0<=idx<n and table[idx]=="H":
            table[idx]=0
            cnt+=1
            break
    # print(cnt)
# 테이블을 순회하며
for i in range(len(table)):
    # 사람을 만났을때 햄버거를 찾아서 먹인다
    if table[i]=='P':
        eat_h(i)
print(cnt)