import sys

input = sys.stdin.readline

def make_recipe (S, B, idx):
    if idx == N:
        if S != 1 and B != 0: #재료를 하나 이상 선택했을 때
            result.append(abs(S - B))
            
        return
    
    make_recipe(S * taste[idx][0], B + taste[idx][1], idx + 1) #재료 선택 O
    make_recipe(S * 1, B + 0, idx + 1) #재료 선택 X

N = int(input())

taste = [list(map(int, input().split())) for _ in range(N)]

result = []

make_recipe(1, 0, 0) #초기값 설정

print(min(result))

#신 맛은 곱, 쓴 맛은 합