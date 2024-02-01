#아니 이럼 7중포문 쓰라는건가..?
import sys
input=sys.stdin.readline
nanjaengyee=[]
breakflag=0
for _ in range(9):
    nanjaengyee.append(int(input()))
nanjaengyee.sort()
height=sum(nanjaengyee)-100 #이러면 가짜 난쟁이 둘의 키 합이고

for i in range(8):
    for j in range(i+1,9):
        if nanjaengyee[i]+nanjaengyee[j]==height:# 가짜난쟁이 찾으면 pop
            nanjaengyee.pop(j)
            nanjaengyee.pop(i)
            breakflag=1
            break
    if breakflag:
        break
    
for i in range(7):
    print(nanjaengyee[i])
