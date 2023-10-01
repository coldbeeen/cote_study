import sys

input = sys.stdin.readline

N = int(input())

rope = []
for i in range(N):
    tmp = int(input())
    rope.append(tmp)

rope.sort() #무게 오름차순으로 정렬

result = 0

for i in range(N): 
    r = rope[i]
    #자신이 최소 무게이므로, 같이 나눠들 수 있는 무게는 본인 무게가 최대
    if r * (len(rope) - i) > result: #같이 나눠 들었을 때 최고 무게를 갱신하였다면
        result = r * (len(rope) - i) #결과 저장

print(result)