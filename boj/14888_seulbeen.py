#연산자 끼워넣기 2랑 차이점 : 연산자의 개수가 딱 맞음
import sys
input=sys.stdin.readline
n=int(input())
nums=list(map(int,input().split()))
operators=list(map(int,input().split()))
min_result=float("inf")
max_result=float("-inf")

# 순서 : + - * /
def operate(result,idx):
    global min_result, max_result
    if idx==n-1:# 다돌았을때
        max_result=max(result,max_result)
        min_result=min(result,min_result)
        return 
    
    for i in range(4):
        if operators[i]!=0:#연산할 연산자가 남아있을 때
            operators[i]-=1
            if i==0: # +
                operate(result+nums[idx+1],idx+1)
            elif i==1: # -
                operate(result-nums[idx+1],idx+1)
            elif i==2: # *
                operate(result*nums[idx+1],idx+1)
            else:# /
                operate(int(result/nums[idx+1]),idx+1)
            operators[i]+=1
            
operate(nums[0],0)
print(max_result)
print(min_result)