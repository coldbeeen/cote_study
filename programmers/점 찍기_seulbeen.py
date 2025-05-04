# 대략 40분정도
"""
x^2+y^2=d^2 를 이용해서 조건문을 일일히 걸었는데 시간초과 발생
가능한 모든 x,y 쌍에 대해서 조건을 확인하는 것이 아니라
x를 기준으로 x의 값에 따라 가능한 y들을 구해보는 방향으로 수정
"""
from itertools import product


def solution(k, d):
    answer = 0
    d_prime = d**2
    cnt = 0

    for x in range(0, d + 1, k):

        # x 값에 따른 y의 최대값
        y = int((d_prime - x**2) ** 0.5)

        # print(f'x : {x} y : {y}')

        # y의 최댓값을 k로 나눈 몫을 구하면 그게 각 x 값마다 가능한 y값들의 개수임
        cnt += y // k

        # 근데 0은 빼고 산출한 것이므로 +1
        cnt += 1

    return cnt

# 시간초과
#     for x,y in product([j*k for j in range(d+1) if j*k<=d],repeat=2):
#         if (x**2+y**2)<=d_prime:
#             # print(x,y)
#             cnt+=1
