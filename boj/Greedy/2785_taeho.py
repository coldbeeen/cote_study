import sys
input = sys.stdin.readline

N = int(input())    # 체인 수
chain = sorted(list(map(int, input().split())))     # 체인의 길이

i = 0
total = 0
needed_chain = len(chain) - 1
if chain[0] > needed_chain:
    total = needed_chain

while total <= needed_chain:
    if total + chain[i] == needed_chain - 1:
        total += chain[i]
        break
    elif total + chain[i] < needed_chain - 1:
        total += chain[i]
        i += 1
        needed_chain -= 1
    else:
        total = needed_chain
        break
if len(chain) == 2:
    total = 1
print(total)