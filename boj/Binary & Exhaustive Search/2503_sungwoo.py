import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
arrs = [map(int, input().split()) for i in range(n)]

cases = list(permutations(range(1,10), 3))  # 가능한 모든 경우의 수 생성
cases = [''.join(map(str, case)) for case in cases]  # 각 case를 문자열 수로 변환
len_of_cases = len(cases)

for arr in arrs:
    num, strike, ball = arr
    num = str(num)
    i = 0

    while i < len_of_cases:  # 모든 경우의 수 순회
        case = cases[i]
        strike_of_case, ball_of_case = 0, 0

        for j in range(3):  # 각 자릿수를 순회하며
            if num[j] == case[j]:  # 해당 case[j]가 num[j]과 같은지 (스트라이크 기준에 부합하는지)
                strike_of_case += 1
            elif num[j] in case:  # 그렇지 않다면(같지 않다면), 해당 case에 포함은 되는지 (볼 기준에 부합하는지)
                ball_of_case += 1

        if strike != strike_of_case or ball != ball_of_case:  # 해당 case의 스트라이크나 볼이 일치하지 않는 경우 경우의 수 리스트에서 삭제
            cases.remove(cases[i])
            len_of_cases -= 1
        else:  # 삭제되지 않은 경우 i 증가
            i += 1
    
print(len(cases))