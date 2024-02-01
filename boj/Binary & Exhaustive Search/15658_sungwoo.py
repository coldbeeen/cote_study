# eval 사용하려 했으나 https://lazymatlab.tistory.com/117 참고하여 사용하지 않음
# 아 permutations 사용하면 안되네요 같은 연산자끼리도 각각 다른 요소로 취급됨
n = int(input())
num_list = list(map(int, input().split()))
oper_list = list(map(int, input().split()))

M = float('-inf')  # 최댓값
m = float('inf')  # 최솟값

def permutations_of_opers(result, i, cur_opers):  # 연산자 순열 탐색 재귀 함수
    global n, M, m

    if i == n or sum(cur_opers) == n - 1:  # 더 이상 계산할 숫자가 없거나 연산자를 n-1개 사용한 경우
        if result > M:  # 최댓값 갱신
            M = result
        if result < m:  # 최솟값 갱신
            m = result
        return

    # 각 인덱스는 +, -, *, / 연산자 개수이므로
    # 현재 연산자 사용 개수인 cur_opers 리스트와, 연산자 개수 리스트인 oper_list 활용하여 4가지의 연산 시도
    if cur_opers[0] < oper_list[0]:  # +를 아직 다 사용하지 않은 경우 + 시도
        cur_opers[0] += 1  # + 사용 횟수 1 증가
        permutations_of_opers(result + num_list[i], i+1, cur_opers)
        cur_opers[0] -= 1  # 원상복구
    if cur_opers[1] < oper_list[1]:
        cur_opers[1] += 1
        permutations_of_opers(result - num_list[i], i+1, cur_opers)
        cur_opers[1] -= 1
    if cur_opers[2] < oper_list[2]:
        cur_opers[2] += 1
        permutations_of_opers(result * num_list[i], i+1, cur_opers)
        cur_opers[2] -= 1
    if cur_opers[3] < oper_list[3]:
        cur_opers[3] += 1
        permutations_of_opers(int(result / num_list[i]), i+1, cur_opers)
        cur_opers[3] -= 1

# 첫 번째 숫자를 result로 초기화하며 시작, 아무 연산자 사용하지 않았으므로 [0,0,0,0] 전달
permutations_of_opers(num_list[0], 1, [0,0,0,0])

print(M)
print(m)