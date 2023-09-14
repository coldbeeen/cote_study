#n이 0이 될때까지 반복

n = 1000 - int(input())
changes = (500,100,50,10,5,1)
cnt = 0
i = 0

while n != 0:
  cnt += n//changes[i] #동전 개수
  n %= changes[i] #나머지 저장
  i += 1


'''
for change in changes: #반복문 형식 백준에서 참고함, 나는 while n != 0으로 풀었는데 이거 어케하는교
    cnt += n//change
    n %= change
'''

print(cnt)