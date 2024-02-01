import sys

input = sys.stdin.readline

N = int(input())

cnt = 0

number = 666

while True:
    tmp = str(number)
    
    if '666' in tmp: #문자열로 변형 후 수행
        cnt += 1
    
    if cnt == N:
        print(number)
        exit(0)
    
    number += 1