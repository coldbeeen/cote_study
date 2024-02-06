import sys
input = sys.stdin.readline

n = int(input())

amounts = list(map(int, input().split()))

result = max(amounts)  # 가장 많은 양의 에너지 드링크에 계속해서 추가!
amounts.remove(result)  # 해당 에너지 드링크 제거 후

for amount in amounts:  # 모두 순회하면서
    result += amount / 2  # 전부 절반씩 추가!

print(int(result) if result % 1 == 0 else result)  # .0 인 경우 소수점 버리기