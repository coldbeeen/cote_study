import sys
from itertools import permutations
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))

per=permutations(arr,n) #순열로 모든 배열의 경우의 수 구함
result=float("-inf")

def abs_sum(nums): #문제의 조건에 맞는 계산 값을 반환
    sum=0
    for i in range(len(nums)-1):
        sum+=abs(nums[i]-nums[i+1])
    return sum

for each_case in per:
    result=max(result,abs_sum(each_case))#최댓값 구하기 
print(result)