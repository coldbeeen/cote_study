# 함수 만들어서 했는데 다 하고 생각해 보니까 그냥 8X8 체스판 두개 리스트로 만들어서 그거랑 바로 비교했어도 됐었겠네;
import sys
input=sys.stdin.readline
def check(arr:list):
    color=['W','B']
    mincnt=float("inf")
    for flag in range(2):
        cnt=0
        for i in range(8):
            for j in range(8):
                if arr[i][j]!=color[(i+j+flag)%2]:
                    cnt+=1
        mincnt=mincnt if mincnt<=cnt else cnt
    return mincnt
n,m=map(int,input().split())

chess=[]

for _ in range(n):
    chess.append(input().rstrip())
min_square=float("inf")

for i in range(n-7):
    for j in range(m-7):
        tmp=[row[j:j+8] for row in chess[i:i+8]]
        cnt=check(tmp)
        min_square=min_square if min_square<=cnt else cnt
print(min_square)


# c언어 처럼 그냥 포인터마냥 인자 전해주고 싶었는데 그게 안돼서 슬라이싱해서 8x8로 자른 배열 하나 더 만들었음
# 백준은 numpy 지원을 안함. 이중 리스트 슬라이싱 하려면 25번째 줄처럼 해야된다네요