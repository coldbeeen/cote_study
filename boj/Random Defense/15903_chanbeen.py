import sys

input = sys.stdin.readline

n, m = map(int, input().split())

num_list = list(map(int, input().split()))

num_list.sort()

for _ in range(m):
    num_list.sort()
    
    tmp = num_list[0] + num_list[1]
    
    num_list[0] = num_list[1] = tmp

print(sum(num_list))

#m번 놀 동안 매번 가장 작은 2개 고르는 게 가장 작은 답을 고르는 법
#sort 쓰면 시간초과 날 줄 알았는데 이게 된다고?