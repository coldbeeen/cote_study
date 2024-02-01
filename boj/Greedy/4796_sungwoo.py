i = 1

while True:
    p, l , v = map(int, input().split())

    if(p == l == v == 0):
        break

    available = 0

    available += v // l * p
    available += min(v % l, p)

    print(f'Case {i}: {available}')
    i += 1