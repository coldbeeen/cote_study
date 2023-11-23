# bisect
# 검사할 배열과 원하는 값을 넣으면 그 값이 들어가야할 인덱스를 반환
# 좌,우 인덱스의 차이를 구하면 중복된 수의 개수를 알 수 있음

from bisect import bisect_left,bisect_right
import sys
input=sys.stdin.readline

n=int(input())
card=list(map(int,input().split()))
card.sort()
m=int(input())
check=list(map(int,input().split()))

for c in check:
    l=bisect_left(card,c)
    r=bisect_right(card,c)
    print(r-l,end=' ')