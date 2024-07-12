from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
num_list = [int(input()) for _ in range(n)]
heapify(num_list)  # heapq 자료구조 사용

result = 0
while len(num_list) > 1:  # 한 묶음으로 합쳐지기 전까지
    num1 = heappop(num_list)  # 가장 작은 카드 뭉치
    num2 = heappop(num_list)  # 두 번째로 작은 카드 문치
    compare = num1 + num2  # 합치기 위한 비교 횟수
    heappush(num_list, compare)  # 합친 카드 뭉치 추가
    result += compare  # 비교 횟수 누적

print(result)  # 비교 횟수 껼과