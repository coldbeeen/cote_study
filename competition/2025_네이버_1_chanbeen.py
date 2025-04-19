#약 25분 소요

import math

def solution(a, cylinder):
    def next_idx(num):
        return (num + 1) % len(cylinder)
    
    numer = 0 #분자
    denomi = 0 #분모
    
    bullets = 0
    
    for i in range(a):
        bullets += cylinder[i] #처음 인덱스부터 a번 발사했을 때 총알 수
    
    left = 0
    right = a - 1 #투 포인터 초기화
    
    for i in range(len(cylinder)):
        bullets -= cylinder[left] #가장 왼쪽값 제거
        left = next_idx(left)
        
        right = next_idx(right)
        bullets += cylinder[right] #새로운 오른쪽값 추가
        
        if cylinder[i]: #방아쇠를 1번 당겼을 때 총알이 발사됨
            continue
        else:
            if not bullets: #총알 발사 안 되는 케이스
                numer += 1
            
            denomi += 1
    
    if not numer: #만족하는 케이스 없음, 확률 0
        return [numer, 1]
    else:
        gcd = math.gcd(numer, denomi)
        
        if gcd != 1: #기약분수
            numer //= gcd
            denomi //= gcd
        
        return [numer, denomi]

#위에 케이스 2개는 무시할 것
#방아쇠를 1번 당겼을 때 총알이 발사되지 않았으므로, 값이 1인 실린더는 분모로도 카운트하면 안 됨
#bullets는 left 인덱스부터 a번 발사했을 때 발사되는 총알의 수
#left, right를 사용하여 투포인터로 bullets 변수 관리 -> 시간 복잡도 O(N)으로 감소