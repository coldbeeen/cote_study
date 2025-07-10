import sys
import heapq

input = sys.stdin.readline

N = int(input())

nums = [list(map(int, input().split())) for _ in range(N)]

idxs = [N - 1 for _ in range(N)]

max_nums = []

for i in range(N):
    max_nums.append(nums[idxs[i]][i]) #마지막열 우선 추가

cnt = 0

while cnt < N:
    max_num = max(max_nums)
    max_idx = (max_nums.index(max_num))

    #print(max_num, max_idx)

    answer = max_num

    idxs[max_idx] -= 1

    max_nums[max_idx] = nums[idxs[max_idx]][max_idx]

    #print(max_nums)

    cnt += 1

print(answer)

#모든 수는 자신의 위에 있는 수보다 크다
#자신의 위에 있는 수보다 큰 것이 보장되고, 다른 열의 수랑은 상관 x

#최대힙 사용했으나 메모리 초과
#2차원 리스트 원소를 모두 사용하면 안되는 듯

#가장 마지막열부터 탐색
#1차원 리스트에서 각 열을 나타내는 인덱스를 두고, 초기 값으로는 마지막열을 할당
#max에 해당하는 값을 pop하고, 그 자리에는 윗 열의 수를 가져와서 넣기

#이래도 메모리 초과가 난다고??
#길이 N짜리 리스트 하나 썼는데?