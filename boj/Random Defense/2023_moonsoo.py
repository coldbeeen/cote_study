import sys

def isPrime(num: int):
    for i in range(2, int(num**(1/2)) + 1):
        # 제곱근까지만 탐색해도 같은 결과를 얻음
        if num % i == 0:
            return 0
    return 1

input = sys.stdin.readline

N = int(input())

# 한 자리 수 소수들의 리스트 생성
primes = [[], [2, 3, 5, 7]]

for i in range(1, N):
    # N 자리수만큼 반복하면서 전 자릿수 숫자들을 한 자릿수 올리고 홀수를 붙여가며 소수인지 판별
    prime_N = []

    for num in primes[i]:
        for digit in range(1, 10, 2):
            # 소수를 찾아야 하므로 짝수에 대한 고려 필요x
            next_num = num * 10 + digit

            if isPrime(next_num):
                prime_N.append(next_num)

    primes.append(prime_N)

for prime_num in primes[N]:
    print(prime_num)