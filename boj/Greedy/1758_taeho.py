# 팁 많이 주는 사람 순으로
# 받는 금액 음수면 continue

import sys
input = sys.stdin.readline

n = int(input())
money = [int(input()) for _ in range(n)]
# 돈을 많이 내는 사람부터 팁을 받기 위해 내림차순으로 정렬
money.sort(reverse= True)
result = 0
# 사람 수 만큼 반복하여 팁을 받는다.
for i in range(n):
    # 사람이 내는 돈 - (받은 등수 - 1) 
    # (받은 등수 - 1) = 0번째로 시작하는 순서와 같다. (0, 1, 2, 3,..)
    tip = money[i] - i
    
    # 팁이 0 보다 크면 팁을 받고 아니면 팁을 받지 않는다.
    if tip > 0:
        result += tip
        
# 팁을 모두 더해 출력
print(result)