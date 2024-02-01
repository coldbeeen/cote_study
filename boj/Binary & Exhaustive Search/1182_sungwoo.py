from itertools import combinations

n, s = map(int, input().split())
num_list = list(map(int, input().split()))
result = 0

for i in range(1, n+1):  # combinations를 활용해 nCi 계산 i는 1~n까지

    combs = combinations(num_list, i)  # nCi 생성

    for comb in combs:  # 조합 순회
        if s == sum(comb):  # 해당 조합의 합이 s라면 result 증가
            result += 1

print(result)