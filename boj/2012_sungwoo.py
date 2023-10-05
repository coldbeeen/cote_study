import sys
input = sys.stdin.readline

n = int(input())
l = sorted([int(input()) for i in range(n)])  # 정렬부터 해주고

result = sum(
    [abs(l[i-1] - i) for i in range(1, n+1)]  # 앞에서부터 1등으로 순위를 부여하여 불만도를 계산 후 합계 계산
)
print(result)