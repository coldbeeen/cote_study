# ㅋㅋ 이런 미친 eval 함수가 있었네
import sys
input=sys.stdin.readline
s=list(input().strip().split('-'))

result=0
tmp=0

temp=list(s[0].split('+'))
for j in temp:
    result+=int(j)
for i in range(1,len(s)):
    temp=list(s[i].split('+'))
    tmp=0
    for j in temp:
        tmp+=int(j)
    result-=tmp
print(result)

