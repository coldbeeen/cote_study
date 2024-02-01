import sys
input = sys.stdin.readline

n = int(input())
losses = sorted(list(map(int, input().split())))  # 근손실 리스트를 정렬

maxLoss = losses.pop() if n % 2 == 1 else 0  # n이 홀수인 경우 맨 마지막(최댓값)을 maxLoss로 설정
for i in range(int(n/2)):  # 양 끝에서 시작하여
    addTwoLoss = losses[i] + losses[-(i+1)]  # 양쪽의 합을 계산해
    if addTwoLoss > maxLoss:  # maxLoss보다 크다면 maxLoss 업데이트
        maxLoss = addTwoLoss

print(maxLoss)