import sys

n, k = map(int, sys.stdin.readline().split())
l = [int(input()) for i in range(n)]
l.reverse()  # 거꾸로 뒤집음 O(1)

result = 0
for i in l:
    q = k // i  # q는 몫
    if q > 0:
        result += q
        k -= i * q  # 사용한 동전만큼 빼주기

print(result)