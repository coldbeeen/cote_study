import sys

N, M, K = map(int, sys.stdin.readline().split())

able_num = N + M - K #인턴십 학생 제외
cnt = 0

while True :
    able_num -= 3
    N -= 2
    M -= 1
    if able_num >= 0 and N >= 0 and M >= 0 :
        cnt += 1
    else :
        break
    
print("%d" %cnt)
