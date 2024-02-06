import sys
n=int(input())
s=list(map(int,sys.stdin.readline().split()))
s.sort()

team=[]
for i in range(len(s)):
    team.append(s[i]+s[len(s)-i-1]) # 코딩 제일 잘치는 럼하고 젤 못치는 럼끼리 붙어야 균형이 맞음
print(min(team))# 팀들중에 나마 코딩 역량 작은팀의 역량 출력