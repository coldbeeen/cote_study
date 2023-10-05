import sys

input = sys.stdin.readline

sick = list(map(str, input().split('-'))) # -로 분리

result = 0

for s in sick[0].split('+'): #첫번째 원소는 따로 처리, 덧셈 진행
    result += int(s)

for s in sick[1:]: 
    for j in s.split('+'): #나머지 원소 각각을 +를 기준으로 다시 분리하여 처리, 뺄셈 진행
        result -= int(j)

print(result)