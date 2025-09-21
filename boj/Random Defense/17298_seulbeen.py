# 오큰수

"""
프그에서 푼 뒤큰수같은데? 그러나 어떻게 풀었는지 가물x2

시간제한 1초
길이 100만
2중 반복문 쓰면 안됨

스택을 사용해서 접근...How?
for문의 인덱스에서 해당하는 오큰수를 찾는 것이 아니라, 매 while문에서 오큰수를 갱신해 나가고, for문은 오큰수의 비교대상으로 stack에만 들어가는것

예시

3 5 6 7 4 9 에서 for문이 6에 해당하는 인덱스를 가리킨다고 가정하면
6의 오큰수를 7,4,9에서 찾는 행위를 하는게 아니라
3의 오큰수를 5로 바꿔주는 행위를 하는것
"""

import sys
input=sys.stdin.readline

n=int(input())

result=[-1 for _ in range(n)]

nums=list(map(int,input().split()))
stack=[]

for idx, num in enumerate(nums):
    while stack and nums[stack[-1]]<num:
        c_idx=stack.pop()
        result[c_idx]=num
    stack.append(idx)
    # print(num)
    # print(stack)
    # print("-"*30)
print(*result)

