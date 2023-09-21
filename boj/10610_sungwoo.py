import sys
import itertools
input = sys.stdin.readline

n = list(input().rstrip())
result = -1

# 모든 자릿수 숫자의 합이 3의 배수이며, 0을 포함하고 있다면 30의 배수 조건 만족
if sum(map(int, n)) % 3 == 0 and '0' in n:  
    n.sort(reverse=True)  # 가장 큰 수로
    result = ''.join(n)  # 합치기

print(result)
