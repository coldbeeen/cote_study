# 이 문제를 고른 이유 : 랜덤카테고리 문제인데, 알고리즙 분류에 그리디, 그래프, BFS가 다있길래 다른 애들은 어떻게 풀지 궁금해서
# a에다가 2를 곱하거나, 1를 붙이는 연산을 하는게 아니라 b에서 2를 나누거나 1을 떼는 연산으로 바꿔서 풀었음
import sys

input=sys.stdin.readline

a,b=map(int,input().split())

cnt=1


while True:
    #2로 나눠지면 나눔
    if b%2==0:
        b//=2
    else:
        tmp=str(b)
        #끝자리가 1인경우에는 1을 떼고
        if tmp[-1]=='1':
            b=int(tmp[:len(tmp)-1])
        #아닌경우는 a로 못만듬
        else:
            cnt=-1
            break
    cnt+=1
    if a==b:
        #같아지면 반복문 탈출
        break
    if a>b:
        #a보다 작아지면 이미 끝난거라서 못만듬
        cnt=-1
        break
print(cnt)