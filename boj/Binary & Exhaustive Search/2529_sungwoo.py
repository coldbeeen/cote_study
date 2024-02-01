n = int(input())
sign = input().split()

def backtrack(cnt):
    global M, m

    if cnt == n + 1:  # 숫자가 '부등호 개수 + 1'개에 도달할 시 최대/최소 갱신 후 종료
        result = ''.join(map(str, num_list))
        if int(result) > int(M):
            M = result
        if int(result) < int(m):
            m = result
        return

    for num in range(10):  # 0 ~ 9까지 시도
        if num in num_list:  # 이미 사용된 숫자는 사용하지 않음
            continue
        if cnt >= 1:  # num과의 비교 대상이 있을 때 비교 연산 시도
            if sign[cnt-1] == '<':  # 해당 부등호일 때
                if not num_list[cnt-1] < num:  # 부등호 불만족 시 continue
                    continue
            else:
                if not num_list[cnt-1] > num:
                    continue

        num_list.append(num)  # 해당 숫자 추가 후
        backtrack(cnt+1)  # 이어서 재귀
        num_list.pop()  # 재귀 후 해당 숫자 제거

num_list = []
M = '0'
m = '9876543210'

backtrack(0)
print(M)
print(m)