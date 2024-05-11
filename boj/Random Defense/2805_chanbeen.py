import sys

input = sys.stdin.readline

N, M = map(int, input().split()) #N : 나무 개수, M : 가져가려는 나무 길이 합

height = list(map(int, input().split()))

start = 0
end = max(height) #최댓값 : 가장 긴 나무 길이

result = 0

while start <= end:
    total = 0
    
    mid = (start + end) // 2 #mid를 기준으로 나무 절단
    
    for h in height:
        if h > mid:
            total += h - mid #mid로 나무를 잘랐을 때 얻는 나무의 양
        
    if total < M: #M보다 total이 작다는 건 mid를 더 낮춰줘야 됨
        end = mid - 1
    else: #M보다 total이 크다는 건 mid를 더 높여줘야 됨
        result = mid
        start = mid + 1

print(result)

#이진 탐색 문제 같다