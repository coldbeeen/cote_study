#약 15분 소요

N, K = map(int, input().split())

idx = 0

nums = [i for i in range(1, N + 1)]

result = []

while nums:
    idx = (idx + K - 1) % N #인덱스 갱신

    result.append(str(nums.pop(idx)))

    N -= 1 #pop한 뒤 N 줄이기

print('<' + ', '.join(result) + '>')