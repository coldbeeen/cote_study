import sys

cnt = 0
while True :
    L, P, V = map(int, sys.stdin.readline().split())
    days = 0
    cnt += 1
    
    if L == 0 and P == 0 and V == 0 :
        break
    
    if L > V % P :
        days = (V // P * L) + V % P #연속된 P일 중 L일 동안만 사용 + 휴가 기간 V일 중 연속된 P일 구간에 걸리지 않는 나머지 휴가 기간
    else :
        days = (V // P * L) + L # 나머지 휴가일수 보다 사용 가능 날짜가 작으면 사용 날짜를 더해줌
    print("Case %d: %d" %(cnt, days))