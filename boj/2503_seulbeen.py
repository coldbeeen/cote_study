# 반복문 돌면서 리스트 삭제하려고 리스트 복사하는법 구글링 

import sys
input=sys.stdin.readline
n=int(input())

#가능한 숫자야구의 경우의 수(123-987)
baseball=[]
for i in range(123,988):
    tmp=str(i)
    if '0' in tmp:
        continue
    if tmp[0]!=tmp[1] and tmp[0]!=tmp[2] and tmp[1]!=tmp[2]:
        baseball.append(tmp)

for i in range(n):
    guess,s,b=map(int,input().split())
    guess=str(guess)#추측

    for item in baseball[::]:#리스트 복사
        cnt_s=0
        cnt_b=0
        for ball in range(3):
            cnt_b+=guess.count(item[ball])# 먼저 볼의 개수를 셈(위치 상관 없이 있으면 볼로 침)
        
        for strike in range(3):# 걔네들 중에서 위치까지 같은애들은 스트라이크로 계산하고 볼 하나 마이너스
            if item[strike]==guess[strike]:
                cnt_s+=1
                cnt_b-=1
        if cnt_s!=s or cnt_b!=b:# 스트라이크랑 볼의 개수가 대답과 다른애들을 소거
            baseball.remove(item)

print(len(baseball))# 남은애들의 수 출력
        
