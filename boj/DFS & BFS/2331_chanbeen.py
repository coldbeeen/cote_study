import sys

input = sys.stdin.readline

A, P = map(int, input().split())

D = []

def calculate(seq):
    num = seq[-1] #마지막 수에서 비교
    
    sum = 0
    for n in str(num):
        tmp = 1
        for i in range(P):
            tmp *= int(n)
        sum += tmp #연산 수행
        
    if sum in seq:
        return seq.index(sum) #반복 등장하는 수가 처음 등장한 인덱스를 반환
    else:
        seq.append(sum)
        return calculate(seq) #다음 원소 비교를 위해 재귀 호출

D.append(A) #첫 원소로는 A를 저장
result = calculate(D)

print(result)