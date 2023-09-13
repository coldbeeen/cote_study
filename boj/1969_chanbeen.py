#구글링해서 풀었음
#각 열별로 가장 많이 나온 알파벳 결과에 더해주고,
#나머지 글자 개수만큼 Hamming Distance에 더해준다
import sys

N, M = map(int, sys.stdin.readline().split())

DNA = [sys.stdin.readline() for _ in range(N)] #이코테 강의 참고했음

result = ""
cnt = 0

for i in range(M):
    a, c, t, g = 0, 0, 0, 0 #각 유전자별로 count해줌
    for j in range(N):
        if DNA[j][i] == 'A':
            a += 1
        elif DNA[j][i] == 'T':
            t += 1
        elif DNA[j][i] == 'C':
            c += 1
        elif DNA[j][i] == 'G':
            g += 1
    if max(a, t, c, g) == a: #알파벳 순서 유의할 것
        result += "A"
        cnt += t + c + g
    elif max(a, t, c, g) == c:
        result += "C"
        cnt += a + t + g
    elif max(a, t, c, g) == g:
        result += "G"
        cnt += a + t + c
    elif max(a, t, c, g) == t:
        result += "T"
        cnt += a + c + g 

print(result)
print(cnt)