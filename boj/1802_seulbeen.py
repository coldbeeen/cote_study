import sys
input=sys.stdin.readline
n=int(input())

for _ in range(n):    
    paper=str(input().rstrip())
    flag="YES"

    while len(paper)>1: # 한번남을때까지 (어차피 그럼 0이든 1이든 접을수있으니까)

        for i in range(len(paper)//2): # 가운데 기준으로 숫자가 대칭이어야 함
            j=len(paper)-1-i
            if paper[i]=='0':
                if paper[j]=='1':
                    pass
                else:
                    flag="NO"
                    break
            else:
                if paper[j]=='0':
                    pass
                else:
                    flag="NO"
                    break
        if flag=="NO":
            break

        paper=paper[0:len(paper)//2] # 접은거 반영해준 후 while문 돌면서 계속 대칭 검사 ㄱㄱ
    
    print(flag)
