import sys

input = sys.stdin.readline

# 카드 개수 n과 더하는 횟수 m 입력. 카드들의 리스트 입력
n, m = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(m):
    # 리스트 정렬
    nums.sort()

    # 앞에서 두 개의 수가 가장 작은 두 수 이므로 이들을 더해 덮어쓴다
    n1, n2 = nums[0], nums[1]

    plus = n1 + n2
    nums[0], nums[1] = plus, plus

# 리스트의 합 출력
print(sum(nums))