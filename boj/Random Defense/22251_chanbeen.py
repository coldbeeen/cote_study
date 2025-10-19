#90분 +@, 구글링

def dfs(depth, cnt, cx):
    if depth >= len(cx): #깊이 계산 변수, return 위한 base case
        if int(cx) == X: #현재 층과 같으면 계산 필요 X
            return 0
        elif 1 <= int(cx) <= N: #가능한 경우의 수
            return 1
        else:
            return 0
        
    result = 0 #가능한 경우의 수 카운팅
    cur = int(cx[depth]) #현재 바꿔줄 숫자
    
    for i in range(10):
        if cur != i and arr[cur][i] <= cnt: #반전 필요 & 반전 가능 횟수 내에 반전 가능
            dx = cx[:depth] + str(i) + cx[depth + 1:] #depth 위치를 i 숫자로 반전
            result += dfs(depth + 1, cnt - arr[cur][i], dx) #반전 횟수만큼 cnt 차감, 반전된 숫자로 재귀 호출
        elif cur == i: 
            result += dfs(depth + 1, cnt, cx) #같으면 반전 필요 X, 재귀 호출
    
    return result

N, K, P, X = map(int, input().split())

if len(str(X)) < K: #X가 K자리가 아닐 경우, 앞 부분은 0으로 표시 위한 작업
    cx = '0' * (K - len(str(X))) + str(X)
else:
    cx = str(X)

num = ['1111110', '0110000', '1101101', '1111001', '0110011', '1011011',
       '1011111', '1110000', '1111111', '1111011']

arr = [] #i에서 j로 반전하는 데 필요한 횟수 저장하는 2차원 행렬

for i in range(10): #i에서 j로 바꿀 때 디지털 반전 횟수 계산
    arr.append([])
    
    for j in range(10):
        if i == j:
            arr[i].append(0) #같은 숫자끼리는 반전 횟수 0
        else:
            d = 0
            
            for h in range(7): #0~9 숫자의 디지털 순회
                if num[i][h] != num[j][h]: #다르면, 반전 필요 
                    d += 1
            
            arr[i].append(d)
            
print(dfs(0, P, cx))

#N이 K자리보다 작다면 빈 공간은 0으로 채우기
#숫자 i에서 j로 반전시키는 데 필요한 횟수를 다 저장해놔야하는데.. -> 2차원 행렬 이용
#0~9의 숫자를 디지털로 표현하기 위한 변수 선언, 각 디지털은 각 인덱스와 매핑됨
#이후 dfs 호출, 각 인덱스마다 반전 해야하는지, 반전하면 횟수는 얼마나 필요한지 계산 후 재귀 호출

#구글링해도 이해하는 데 너무 오래걸렸다. num 변수부터 해서 생각해내기 쉽지 않았던 문제