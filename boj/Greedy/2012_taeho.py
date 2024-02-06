# 오름차순 정렬해서 각자 최대한 자기 자리에 가깝게 만들어두고
# sum(|예상등수-실제등수|)
import sys
input = sys.stdin.readline

N = int(input())
num_list = [int(input()) for _ in range(N)]
num_list.sort()
answer = 0

for i in range(N) :
  answer += abs(i+1 - num_list[i])

print(answer)


