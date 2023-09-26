import sys
input=sys.stdin.readline
s=input().strip()
c=input().strip()
cnt=0
i=0
while i<=len(s)-len(c):
    if s[i:i+len(c)]==c: # 문자열비교
        cnt+=1
        i+=len(c)
        continue
    i+=1
print(cnt)
#커밋했는데 뭔가 문제가 생겨서 다시 커밋함

