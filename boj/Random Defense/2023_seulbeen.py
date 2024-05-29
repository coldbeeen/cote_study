import sys
input=sys.stdin.readline

n=int(input())

#소수 판별 함수
def prime(number):
    for i in range(2,int(number**(0.5)+1)):
        if number%i==0:
            return False
    return True

#알고리즘이 백트래킹이라서 함수이름이 이렇긴한데 백트래킹이 아니라 DFS인듯
def backtracking(number):
    if len(str(number))==n:
        print(number)
    else:
        # 뒤에 짝수가 붙으면 무조건 2로 나눠지므로 홀수만 붙여야됨
        for i in range(1,10,2):
            tmp=10*number+i
            if prime(tmp):
                backtracking(tmp)
backtracking(2)
backtracking(3)
backtracking(5)
backtracking(7)
