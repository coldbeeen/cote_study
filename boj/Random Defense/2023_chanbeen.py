#마감 기한 초과
import sys

input = sys.stdin.readline

def isPrime(num):
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    
    return True

def backtracking(num):
    if len(str(num)) == N:
        print(num)
    else:
        for i in range(1, 10): #어차피 0으로 끝나면 소수 불가
            if i % 2 == 0: #짝수여도 소수 불가
                continue
            
            if isPrime(num * 10 + i):
                backtracking(num * 10 + i)

N = int(input())

backtracking(2)
backtracking(3)
backtracking(5)
backtracking(7) #한 자리 수 중 소수는 2, 3, 5, 7

#소수 판별 문제
#소수 : 약수가 1과 자기 자신뿐인 수, 1은 소수가 아니다
#7을 소수로 판단하는 건 금방하겠지만, 733같은 수를 소수로 판단하는 데에는 시간이 걸릴 것이다
#N이 4만 되어도 많은 반복이 필요하다
#조건을 만족하는 수만 뒤쪽에 수를 붙여서 탐색하는 알고리즘
