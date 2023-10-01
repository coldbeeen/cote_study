# 일단 무조건 4번 다 써야되니까 순서 상관없이 4번째 위치는 고정임!
# 4회 이상 이동할 수 있는 경우 1.(최소 올라갔다왔다 할 3칸 필요) 2.(4회 이동후 7번째 칸에 있어야함, 즉 7열까지 있어야 함)
''' 1. 2칸 위로, 1칸 오른쪽
    2. 1칸 위로, 2칸 오른쪽
    3. 1칸 아래로, 2칸 오른쪽
    4. 2칸 아래로, 1칸 오른쪽
'''
import sys
input=sys.stdin.readline    
n,m=map(int,input().split())
if 7<=m and 3<=n: # 4회이상 무빙가능(4회 이후에는 이동방법 어차피 제약없음)
    block_cnt=5
    m-=7
    block_cnt+=m
else: #4회도 못채움(이동방법 제약없음)
    if n==1:#아무데도 못감
        block_cnt=1
    elif n==2:# 수직으로 한칸밖에 못움직이는경우(오른쪽으로 2칸씩밖에 못감)
        block_cnt= 4 if 7<m else (m+1)//2
    else:# 수직이동은 자유로운 경우(오른쪽으로 1칸씩 갈수 있음)
        block_cnt= 4 if 3<m else m
print(block_cnt)