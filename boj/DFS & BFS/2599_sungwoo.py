import sys
input = sys.stdin.readline

n = int(input())
tbl = [list(map(int, input().split())) for _ in range(3)]

print(tbl)
result = []
for i in range(3):
    for j in range(3):
        if i == j:
            continue

        pair_num = min(tbl[i][0], tbl[j][1])
        tbl[i][0] -= pair_num
        tbl[j][1] -= pair_num
        result.append(pair_num)

rest = sum(sum(row) for row in tbl)

if rest == 0:
    print(1)
    for i in range(3):
        print(result[2*i], result[2*i+1])
else:
    print(0)