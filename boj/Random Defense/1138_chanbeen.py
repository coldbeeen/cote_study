#약 35분 소요

N = int(input())

p = list(map(int, input().split()))

answer = [0] * N

for i in range(N):
    cnt = 0

    for j in range(N):
        if answer[j] == 0:
            if cnt == p[i]: #왼쪽에 있는 더 큰 사람 수와 일치
                answer[j] = i + 1 #i번째 사람이 서야할 위치

                break

            else:
                cnt += 1

print(' '.join(map(str, answer)))