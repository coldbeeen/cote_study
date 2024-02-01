N, M = map(int, input().split())

l = []
for i in range(N):
    l.append(input())

dicts = [{} for i in range(M)]

for i in range(M):

    each = []
    for j in range(N):
        each.append(l[j][i])
    
    m = sorted(list(set(each)))
    for k in m:
        dicts[i][k] = each.count(k)

result = ''
result_sum = 0
for dict in dicts:
    max_ch = max(dict, key=dict.get)  # 가장 겹치는 DNA가 많은 문자
    result += max_ch
    result_sum += N - dict[max_ch]  # 다른 문자 개수

print(result)
print(result_sum)