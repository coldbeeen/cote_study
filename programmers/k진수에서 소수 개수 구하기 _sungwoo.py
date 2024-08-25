from math import sqrt

def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def solution(n, k):

    answer, k_number = 0, ''

    # k진수로 변환
    while n > 0:
        k_number = str(n % k) + k_number
        n //= k

    split_k_number = k_number.split('0')  # 0을 기준으로 문자열을 나눔

    # 나눠진 요소들을 대상으로 소수인지 판별
    for number in split_k_number:
        if number != '' and is_prime(int(number)):
            answer += 1

    return answer  # 소수 개수 출력