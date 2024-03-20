# 조합의 공식을 이용했음
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
m=min(m,n-m)# 100C6=100C94 이르모 둘중에 작은게 연산 효율성이 좋을 것
up=1 # 분모
down=1 # 분자

for i in range(n,n-m,-1):
    up*=i
for i in range(1,m+1):
    down*=i

print(up//down)
"""
10C3= 10X9X8/3X2X1
"""