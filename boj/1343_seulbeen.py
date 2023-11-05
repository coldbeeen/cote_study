#너무 급하게 생각안하고 뇌뺴고 풀어서 코드 더러움 ㅈㅅㅈㅅ...
#사실 더 좋은 방법이 있을거 같은데 보드판의 범위가 50이라서 배열 여러개 써도 메모리 문제 없을거같았음
import sys
input=sys.stdin.readline
board=input().rstrip()
cnt=0
poliomino=[]
result=[]

#.이 나오기 전까지 X의 개수를 세서 개수를 저장하는 배열 만듬
for i in range(len(board)):
    if board[i]=='X':
        cnt+=1
    else:
        poliomino.append(cnt)
        cnt=0
poliomino.append(cnt)
#남은 개수가 4로 나누어지면 A로 채우고, 2가 남으면 B로 채우고, 둘다 아니면 -1 출력하고 exit
for item in range(len(poliomino)):
    if poliomino[item]%4==0:
        for i in range(poliomino[item]):
            result.append('A')
    elif poliomino[item]%4==2:
        for i in range(poliomino[item]//4*4):
            result.append('A')
        for i in range(2):
            result.append('B')
    else:
        print('-1')
        exit()
    if item<len(poliomino)-1:
        result.append('.')

for item in result:
    print(item,end='')

