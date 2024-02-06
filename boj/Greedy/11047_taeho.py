N, K = map(int, input().split()) 
coin = list()
sum = 0

for i in range(N):
    coin.append(int(input()))

for i in reversed(range(N)):
    sum += K//coin[i] #K를 코인으로 나눈 몫을 더해줌
    K = K%coin[i] #나머지로 계속 반복

print(sum)