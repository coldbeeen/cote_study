# 구글링

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
puddles = [list(map(int, input().split())) for _ in range(N)]
puddles.sort()

plank = puddles[0][0]
num_needed = 0
for s, e in puddles:
  if plank > e:
    continue
  elif plank < s:
    plank = s
  
  dist = e - plank

  rem = 1
  if dist % L == 0:
    rem = 0
  
  count = dist // L + rem
  plank += count * L
  num_needed += count

print(num_needed)