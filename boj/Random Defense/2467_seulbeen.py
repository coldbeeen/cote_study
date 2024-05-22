import sys
# 조합쓰면 시간초과
input=sys.stdin.readline

n=int(input())
yongaeks=list(map(int,input().split()))

#0번째 인덱스와 끝 인덱스를 초기 두용액의 인덱스로 지정
first, second = 0, len(yongaeks)-1

#minus plus는 반복문을 돌기 위함
minus,plus=first,second

#최적의 특성값 저장될 예정
feature=float("inf")

while minus!=plus:
    #minus와 plus인덱스의 혼합용액의 특성값 구함
    gap=yongaeks[plus]+yongaeks[minus]

    #최적의 특성값보다 0에 가까울때 인덱스와 특성값 갱신
    if abs(gap)<feature:
        feature=abs(gap)
        first=minus
        second=plus

    """오름차순으로 정렬되어있음
    혼합특성값이 양수일때는 절댓값이 더 작은 양수를 더해줘야 특성 값이 0에 가까워지고(절댓값이 더 작은 음수를 더해주면 차이가 더욱 커짐), 
    반대의 경우도 동일
    """

    if gap>0:
        plus-=1
    elif gap<0:
        minus+=1

    #특성값 0이면 인덱스 갱신 후 즉시 탈출
    else:
        first=minus
        second=plus
        break

print(f"{yongaeks[first]} {yongaeks[second]}")

                

