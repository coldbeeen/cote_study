# 팁 낮은 놈들을 제일 뒤로 빼야 이득인가? 어차피 음수의 절댓값에 상관없이 0원이니까? => 예시 보니까 얘가 맞네
# 팁 낮은 애들을 살려서 앞에 놔야 이득인가? 일단 양수가 많으면 이득? 
import sys
input=sys.stdin.readline
n=int(input())
waiting=[]
for _ in range(n):
    waiting.append(int(input()))
waiting.sort(reverse=True)
cnt=0
for i in range(len(waiting)):
    tip= 0 if waiting[i]-i <=0 else waiting[i]-i
    cnt+=tip
print(cnt)