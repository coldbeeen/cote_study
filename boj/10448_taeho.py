import sys
input = sys.stdin.readline

max = [n*(n+1)//2 for n in range(1, 46)]
eureka = [0] * 1001 # 이 줄은 구글링

for i in max:
    for j in max:
        for k in max:
            if i + j + k <= 1000:
                eureka[i+j+k] = 1 # 삼각수 합으로 표현가능
    
n = int(input())

for _ in range(n):
    print(eureka[int(int(input()))])