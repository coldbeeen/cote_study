import sys
input = sys.stdin.readline

n = int(input())

tips = sorted([int(input()) for i in range(n)], reverse=True)  # 팁을 입력받고 높은 순서로 정렬

result = 0

for i in range(n):
    realTip = max(tips[i] - i, 0)  # 실제 팁을 계산해준 후
    result += realTip  # 팁을 누적!

print(result)