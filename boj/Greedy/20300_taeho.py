import sys 
input = sys.stdin.readline

n = int(input()) #운동기구 개수
lose = list(map(int, input().split()))
lose.sort() #오름차순으로 정렬

result = lose[-1] #가장 큰 근손실 정도

if n%2==1: #홀수일 경우 하나만 사용하는 기구는 근손실이 가장 큰 기구여야 함
    for i in range(n//2): #2개씩 더할 예정이므로 절반만
        tmp = lose[i]+lose[n-i-2] #리스트에서 제일 작은 값과 제일 큰 값을 더함
        if result < tmp: #result는 현재 가장 큰 값, tmp값이 더 크다면 바꿔줌
            result = tmp

elif n%2==0: #짝수일 경우에도 같은 방법으로 해준다
    for i in range(n//2):
        tmp = lose[i]+lose[n-i-1]
        if result < tmp:
            result = tmp

print(result)