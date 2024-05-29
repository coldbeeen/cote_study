from math import sqrt

def is_prime(x):  # 소수 판별 함수
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def backtrack(n):  # 백트래킹 함수
    if not is_prime(n):  # 소수가 아니라면 재귀 종료
        return

    if start <= n <= end:  # 소수이고, 유효한 범위 내에 도달했다면 해당 값 출력 후 재귀 종료
        print(n)
        return

    for i in range(1, 10, 2):  # n에 홀수를 붙여 후보군 탐색 (짝수를 붙인 수는 소수가 아님)
        backtrack(n * 10 + i)

n = int(input())
start = 10 ** (n-1)
end = (10 ** n) - 1

for i in range(1, 10):  # 1~9에 홀수를 붙이며 신기한 소수를 탐색함
    backtrack(i)