#구글링
def check(a, b, op):
  if op == '<':
    if a > b: return False
  if op == '>':
    if a < b: return False
  return True

def dfs(cnt, num):
  if cnt == k+1:
    answer.append(num)
    return
  
  for i in range(10):
    if visited[i]: continue

    if cnt == 0 or check(num[cnt-1], str(i), signs[cnt-1]):
      visited[i] = 1
      dfs(cnt+1, num+str(i))
      visited[i] = 0

k = int(input())
signs = list(input().split())
visited = [0]*10
answer = []
dfs(0, '')
answer.sort()
print(answer[-1])
print(answer[0])
# import sys
# from itertools import permutations
# input=sys.stdin.readline
# n=int(input())
# bdh=input().split()
# max_n=float("-inf")
# min_n=float("inf")
# cases=permutations(range(10),n+1)
# print(list(cases))
# for each_case in cases:
#     flag=1
#     for i in range(bdh):
#         if bdh[i]=='>':
#             if each_case[i]<each_case[i+1]:
#                 flag=0
#                 break
#         else:
#             if each_case[i]>each_case[i+1]:
#                 flag=0
#                 break
#     if flag==1:
#         max_n=max(max_n,each_case)
#         min_n=min(min_n,each_case)
# print(max)