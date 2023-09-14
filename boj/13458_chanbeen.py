import sys

N = int(sys.stdin.readline())
A_i = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

cnt = 0

for i in range(N): #총감독관은 시험장 당 한 명씩
    A_i[i] -= B
    cnt += 1
    if A_i[i] < 0 : #뺄셈으로 수험장 인원이 -가 될 경우를 대비
        A_i[i] = 0

for i in range(N): #부감독관은 여러명
    cnt += A_i[i] // C
    if A_i[i] % C != 0: #나머지 인원이 남아있다면
        cnt += 1

print(cnt)