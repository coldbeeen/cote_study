import sys
input=sys.stdin.readline
n=int(input())

for _ in range(n):
    yureka=int(input())
    result=0
    breakflag=0 #반복문 탈출용
    for i in range(1,yureka+1):
        for j in range(i,yureka+1):
            for k in range(i,yureka+1):

                tri=(i*(i+1)+j*(j+1)+k*(k+1))/2 #삼각수 세개 합
                if tri > yureka:# 이미 넘었으면 다음 수로
                    break

                if tri==yureka:# 찾았으면 result바꾸고 탈출
                    result=1
                    breakflag=1
                    break
            if breakflag:
                break
        if breakflag:
            break
    print(result)#결과출력