#약 10분 소요

N = int(input())

serials = list(input().rstrip() for _ in range(N))

serials.sort(key = lambda x: (len(x), sum(int(c) for c in x if c.isdigit()), x))

for s in serials:
    print(s)

#시리얼번호 정렬하기
#조건
#A와 B 중 길이가 짧은 게 앞으로
#길이 같으면 숫자인 것만 합산해서 더 작은 게 앞으로
#숫자 합산도 같으면 사전순 (숫자가 알파벳보다 사전순으로 앞)