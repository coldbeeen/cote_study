import sys

input = sys.stdin.readline

N, M = map(int, input().split())

time = list(map(int, input().split()))

start = max(time) #블루레이 개수가 len(time)개일 때 다 담으려면은 가장 큰 요소의 크기로 시작값을 설정해줘야 됨
end = sum(time)

result = 0

while start <= end:
    mid = (start + end) // 2 
    
    cnt = 1 #쪼개는 그룹의 수
    total = 0
    
    for t in time:
        total += t
        if total > mid:
            cnt += 1 #강의 길이가 블루레이보다 넘쳐서 그룹을 더 쪼개줘야됨
            total = t #넘치기 전 값으로 돌려놓기
    
    if cnt > M: #그룹이 더 많이 쪼개졌으니 mid를 큰 절반쪽으로 이동시켜줘야 함
        start = mid + 1
    else: #그룹이 덜 쪼개졌다면 그 중 최소값이 result로 저장될 것임
        end = mid - 1
        result = mid
        
print(result)