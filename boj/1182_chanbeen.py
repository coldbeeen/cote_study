import sys

input = sys.stdin.readline

N, S = map(int, input().split())

num = list(map(int, input().split()))

cnt = 0

def count(sub_sum, idx): #재귀함수의 기초 형태 구글링 했음 : 리턴, 조건문, 재귀 호출
    global cnt #cnt 관리 위해 전역변수로 선언 필요
    
    if idx == N:
        return
    
    sub_sum += num[idx]
    
    if sub_sum == S:
        cnt += 1
    
    count(sub_sum, idx + 1) #요소 선택 o
    count(sub_sum - num[idx], idx + 1) #요소 선택 x

count(0, 0)
print(cnt)

#리스트의 각 요소별로 선택하거나, 안 하거나로 이진 트리 구성
#이후 선택했을 때, 안 했을 때로 각각 재귀함수 호출 = 백 트래킹
#S와의 비교 조건문 이전에 덧셈을 해주는 것이 중요함
#S가 0인 경우에는 초기값이 0이라서 덧셈을 미리 안 하면 cnt에 N개가 추가되기 때문

#재귀함수를 구성할 때 중요한 요소 3가지
#1. 리프를 찍었을 때 돌아갈 수 있는 return 조건
#2. 함수에 들어가는 인자 값을 재귀 호출 시마다 변경
#3. 리프를 찍고 이전 단계로 돌아갔을 때는 이전 값으로 돌려놓기
#   = 재귀함수 내에서 리스트같은 자료형을 변수로 다루는 것은 위험할 수 있음