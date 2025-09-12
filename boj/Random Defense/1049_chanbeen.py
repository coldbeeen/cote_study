#약 30분 소요

N, M = map(int, input().split())

brands = [list(map(int, input().split())) for _ in range(M)]

answer = 0

num_s = N // 6 #share
num_r = N % 6 #remainder

min_p = 1e9 #package
min_s = 1e9 #single

for i in range(M):
    min_p = min(min_p, brands[i][0], brands[i][1] * 6) #패키지 가격 or 단품 6개 구매 가격 중 싼 것
    min_s = min(min_s, brands[i][1])

answer += num_s * min_p
answer += num_r * min_s

answer = min(answer, min_p * (num_s + 1)) #개수 딱 맞춰사기 vs 패키지 단위로 개수 넘치게 사기

print(answer)

#인덱스 0 : 6개 한번에 살 때 가격
#인덱스 1 : 1개씩 살 때 가격

#N을 6으로 나눈 몫만큼은 모든 브랜드의 패키지 가격 or 낱개로 6개 가격 중 더 싼걸로 선택
#N을 6으로 나눈 나머지는 낱개 가격 중 가장 싼 가격으로 선택
#개수를 딱 맞춰 사는게 아니라, 오버되서 샀을 때 오히려 금액이 더 싼 경우가 있음