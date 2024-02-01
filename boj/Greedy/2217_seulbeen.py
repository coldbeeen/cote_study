import sys
input=sys.stdin.readline
n=int(input())
r=[]
for i in range(n):
    r.append(int(input()))
r.sort(reverse=True) # 밧줄 내림차순 정렬
m=r[0] # 최댓값 설정 => 제일 튼튼한 밧줄
for i in range(1,len(r)):
    avr_weight=r[i]*(i+1) # 밧줄 하나씩 추가해가며 분산해서 들때의 총 하중
    m= m if avr_weight<=m else avr_weight # 그거랑 최댓값이랑 비교해서 갱신
print(m)
        