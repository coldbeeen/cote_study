import sys

input = sys.stdin.readline

N = int(input())

drink = sorted(list(map(int, input().split())))

for i in range(N - 1):
    drink[-1] += drink[i] / 2 #가장 많은 양의 드링크에 하나씩 반띵해서 더해주는 것이 최대

print(drink[-1])