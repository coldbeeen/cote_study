n = int(input())

def is_palindrome(n):  # 팰린드롬 검사
    n_str = str(n)  # 문자열로 변환한 후
    n_str_len = len(n_str)

    for i in range(n_str_len // 2):  # 양 끝부터 차례로 같은지 검사
        if n_str[i] != n_str[n_str_len - 1 - i]:
            return False
    return True

def is_prime(n):  # 소수 검사
    cnt = 0

    for i in range(1, n+1):  # 1 ~ n까지 나누어 떨어지게 하는 수 cnt 증가
        if n % i == 0:
            cnt += 1
    return True if cnt == 2 else False  # 2개인 경우 소수


while True:
    if is_palindrome(n) and is_prime(n):  # 팰린드롬 및 소수 검사
        break

    n += 1

print(n)