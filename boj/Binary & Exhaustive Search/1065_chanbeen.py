import sys

input = sys.stdin.readline

N = int(input())

cnt = 0

for i in range(1, N + 1):
    nums = [int(num) for num in str(i)]
    
    if len(nums) < 3:
        cnt += 1
    else:
        if (nums[0] + nums[-1]) / 2 == nums[1]:
            cnt += 1
            
print(cnt)

#입력 범위가 셋째 자리 수니까 가능한 방법
#입력 범위가 더 넓어지면 어떻게 해결해야될까?
#nums에서 nums[j + 1] - nums[j]를 각 원소마다 확인하여 한번이라도 다르면 flag를 바꾸게 하면 될 듯