# n이 소수가 아니라면, 무조건 2~ 루트n 내에 약수가 존재하고, n의 약수는 저 범위의 약수와, n을 그 수로 나눈 몫으로 이루어짐
# ex, 100의 약수는  2~루트100(10) 내의 1,2,4,5,10, 그리고 이 수들로 나눈 몫 100,50,25,20,10
# 따라서 2~루트n 내에 약수가 없다면 n은 소수
import sys
input=sys.stdin.readline
n=int(input())


def palindrome(num):# palindrome 검사
    for i in range(len(num)//2):
        if num[i]!=num[-1-i]:
            return False
    return True

def prime_number(num): # 소수 검사
    if num==1:
        return False # 1은 소수가 아님
    
    max_prime=int(num**0.5)
    for i in range(2,max_prime+1): # 2 ~ 루트N까지 num의 약수가 존재하면 소수가 아님
        if num%i==0:
            return False
    return True

while True:
    if prime_number(n):
        if palindrome(str(n)):
            print(n)
            break
    n+=1
        

