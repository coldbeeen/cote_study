n = int(input())
num_list = list(map(int, input().split()))
oper_list = list(map(int, input().split()))

M = float('-inf')  # 최댓값
m = float('inf')  # 최솟값

def oper_calc(x, y, oper):  # oper에 따른 알맞은 연산 수행
    if oper == 0:
        return x + y
    elif oper == 1:
        return x - y
    elif oper == 2:
        return x * y
    else:
        return int(x/y)

def permutations_of_opers(result, i):  # 연산자 순열 탐색 재귀 함수
    global n, M, m
    if i == n:  # 연산자 모두 소진 시
        if result > M:  # 최댓값 갱신
            M = result
        if result < m:  # 최솟값 갱신
            m = result
        return

    # 각 인덱스는 +, -, *, / 연산자 개수. 연산자를 사용할 때 마다 해당 인덱스의 값 1 감소
    for oper_idx in range(4):
        if oper_list[oper_idx] > 0:  # 연산자를 아직 다 사용하지 않은 경우 시도
            oper_list[oper_idx] -= 1
            permutations_of_opers(oper_calc(result, num_list[i], oper_idx), i + 1)
            oper_list[oper_idx] += 1  # 원상 복구

# 첫 번째 숫자를 result로 초기화하며 시작
permutations_of_opers(num_list[0], 1)

print(M)
print(m)