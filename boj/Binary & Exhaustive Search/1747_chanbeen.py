import sys

input = sys.stdin.readline

N = int(input())

def isPalindrome(num): #팰린드롬
    num = str(num)
    
    for i in range(len(num) // 2):
        if num[i] != num[len(num) - 1 - i]:
            return False
    
    return True

def isPrimeNumber(num): #소수
    if num == 1: #2는 짝수 중 유일한 소수라 특이 케이스
        print(2)
        exit(0) #메인함수 종료 코드인데, 1 넣으면 런타임 에러남
    
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True

while True:
    if isPalindrome(N) and isPrimeNumber(N):
        print(N)
        
        break
    
    N += 1