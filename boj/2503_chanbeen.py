#구글링
import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

num_list = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3)) #모든 경우의 수를 만들고, 제거해나가는 방식

for _ in range(N):
    num, s, b = map(int, input().split())
    num = list(str(num)) #3자리 숫자를 자릿수 분리하여 리스트로 저장
    
    cnt = 0
    
    for i in range(len(num_list)):
        strike = ball = 0 #일단 0으로 초기화
        i -= cnt
        
        for j in range(3):
            if num_list[i][j] == num[j]: #입력받은 숫자와 리스트의 숫자가 자릿수까지 같으면
                strike += 1 #스트라이크
            elif num[j] in num_list[i]: #자릿수는 다르지만 안에 존재한다면
                ball += 1 #볼
        
        if (strike != s) or (ball != b): #영수가 생각하는 숫자와 조건이 맞지 않다면
            num_list.remove(num_list[i]) #모든 경우의 수가 있는 리스트에서 해당 숫자를 제거
            cnt += 1

print(len(num_list))