import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())
on_table = [int(input()) for _ in range(N)]

sushi = on_table[0:k] #k가지 연속 먹기, 초기화값

ans = 0

for i in range(N): 
    s = sushi.copy() #깊은 복사
    
    s.append(c)
    
    ans = max(ans, len(list(set(s))))
    
    sushi.pop(0)
    sushi.append(on_table[(k + i) % N]) #회전초밥이니까 마지막 입력과 첫 입력이 연속된 k개에 해당될 수 있음

print(ans)