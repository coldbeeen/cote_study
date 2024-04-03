import sys
input=sys.stdin.readline

def flip(r,c):
    for i in range(r,r+3):
        for j in range(c,c+3):
            if matA[i][j]=='0':
                matA[i][j]='1'
            else:
                matA[i][j]='0'



n,m=map(int,input().split())

matA=[]
matB=[]
cnt=0

for _ in range(n):
    matA.append(list(input().rstrip()))
for _ in range(n):
    matB.append(list(input().rstrip()))
if matA==matB:
    print(0)
    exit()
if n<3 or m<3:
    print(-1)
    exit()

for i in range(n-2):
    for j in range(m-2):
        if matA[i][j]!=matB[i][j]:
            flip(i,j)
            cnt+=1
if matA==matB:
    print(cnt)
else:
    print(-1)

# 왜 flip함수 직후에 검사를 한 후 break 하는 건 틀렸다 나오지??? 똑같은거 아닌가?