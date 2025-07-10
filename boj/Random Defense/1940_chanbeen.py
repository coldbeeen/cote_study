N = int(input())
M = int(input())

nums = list(map(int, input().split()))

nums.sort()

left = 0
right = N - 1

cnt = 0

while left < right:
    armor = nums[left] + nums[right]
    
    if armor < M:
        left += 1
    elif armor > M:
        right -= 1
    else:
        cnt += 1
        left += 1
        right -= 1
        
print(cnt)

#2개의 재료를 따로 관리 -> 투포인터 접근
#투포인터 활용 위해 정렬
#재료 더해서 M과 일치해야 갑옷 만들 수 있음
#갑옷 만든 뒤에는 2개 인덱스 모두 조정