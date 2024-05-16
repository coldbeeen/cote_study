
def calculate(l, r):
    global L, R, diff

    cur_diff = abs(ph[l] + ph[r])
    if cur_diff <= diff:
        L, R = l, r
        # print(L, R)
        diff = cur_diff



N = int(input())

ph = list(map(int, input().split()))

# 양쪽 끝을 l, r 포인터로 관리하고 초기 값을 구합니다
l, r = 0, len(ph) - 1
diff = abs(ph[l] + ph[r])
L, R = l, r

while l < r:
    calculate(l, r)

    if abs(ph[l]) > abs(ph[r]):
        l += 1
    else:
        r -= 1


# print(L, R)
print(ph[L], ph[R])

"""
문제:

정렬된 숫자의 리스트에서 두 수의 합이 0에 가장 가까운 조합 찾기
---------------------------------------------------------------------------------
풀이:

숫자의 합의 절댓값의 최소를 찾는 문제와 같다.
시작과 끝을 투포인터로 관리하면서 l < r일 때까지 반복한다.
l, r의 갱신 조건은 둘 중 절댓값이 더 큰 녀석을 옮겨 합을 더 작게 만드는 경우의 수를 찾도록 한다.
(무조건 합이 작아지는 것은 아님!)
"""