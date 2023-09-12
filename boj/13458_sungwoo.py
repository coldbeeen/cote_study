n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

sup_cnt = 0

for i in range(n):
    sup_cnt += 1
    if a[i] <= b:
        continue
    a[i] -= b

    sup_cnt += (a[i]-1) // c + 1
    print()

print(sup_cnt)

