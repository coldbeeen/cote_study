#구글링 했습니다...ㅜㅜ

import sys
from itertools import permutations
input=sys.stdin.readline
n=int(input())
num=list(map(int,input().split()))
num_of_operators=list(map(int,input().split()))# 덧 뺄 곱 나
max_result=float("-inf")
min_result=float("inf")
def operate(result,num_idx):
    global max_result, min_result # 이거 없으면 오류남. 재귀함수 돌때 초기화되지 않기 위해 전역변수로
    if num_idx==n-1: # 종료조건: 숫자 다 돌았을 때
        max_result=max(result,max_result)
        min_result=min(result,min_result)
        return
    for i in range(len(num_of_operators)):
        if num_of_operators[i]!=0:
            num_of_operators[i]-=1
            if i==0:# +
                operate(result+num[num_idx+1],num_idx+1)
            elif i==1:# -
                operate(result-num[num_idx+1],num_idx+1)
            elif i==2:# *
                operate(result*num[num_idx+1],num_idx+1)
            else:# /
                if result<0:
                    result=-result
                    operate(-(result//num[num_idx+1]),num_idx+1)
                else:
                    operate((result//num[num_idx+1]),num_idx+1)
            num_of_operators[i]+=1
operate(num[0],0)
print(max_result)
print(min_result)
                

# operators=""
# 순열 쓰면 시간초과
# def operate(o):
#     result=num[0]
#     for i in range(len(o)):
#         if o[i]=='+':
#             result+=num[i+1]
#         elif o[i]=='-':
#             result-=num[i+1]
#         elif o[i]=='*':
#             result*=num[i+1]
#         else:
#             result//=num[i+1]
#     return result

# for i in range(len(num_of_operators)):
#     if i==0:
#         operators+='+'*num_of_operators[i]
#     elif i==1:
#         operators+='-'*num_of_operators[i]
#     elif i==2:
#         operators+='*'*num_of_operators[i]
#     else:
#         operators+='/'*num_of_operators[i]

# case_operator=permutations(operators,n-1)

# max_result=float("-inf")
# min_result=float("inf")
# for each_case in case_operator:
#     max_result=max(max_result,operate(each_case))
#     min_result=min(min_result,operate(each_case))
# print(f'{max_result}\n{min_result}')
