import sys
input = sys.stdin.readline

k = int(input())

size, i = 1, 1
while size < k:  # k보다 크거나 같은 2의 제곱인 수 찾기
    size = 2 ** i
    i += 1
print(size, end=' ')

result = 0
if size > k:  # 쪼개야 하는 경우
    while size > 0:
        size //= 2  # 쪼개기
        result += 1  # 쪼갠 횟수
        if k % size == 0:  # 쪼개고 나눠 먹는 조건 만족 시 break
            break

print(result)