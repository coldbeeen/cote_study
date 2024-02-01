import sys

input = sys.stdin.readline

N = int(input())

chain = list(map(int, input().split()))

chain.sort(reverse=True) #시간복잡도를 위해 역순 정렬

idx = N - 1
cnt = 0

if N == 2: #체인 2개면 고리 하나로 묶으면 끝
    cnt = 1
else:
    while True:
        chain[idx] -= 1 #끝에서부터 체인 하나씩 해체
        cnt += 1
        
        if chain[idx] == 0: #다 해체했으면
            
            if cnt == len(chain) - 1: #idx에서 딱 하나 체인이 남았고, 이를 긴 체인에 덧붙이면서 완성된 경우
                break
            
            chain.pop() #리스트에서 제거
            idx -= 1
        
        if cnt == len(chain) - 1: #idx의 체인을 딱 맞게 소비했거나, 2개 이상 남긴 채로 하나의 긴 체인을 연결한 경우
            break

print(cnt)