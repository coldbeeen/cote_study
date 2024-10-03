def solution(cap, n, deliveries, pickups):  
    deliveries = deliveries[::-1]  
    pickups = pickups[::-1]  
    answer = 0  

    d = 0  
    p = 0  

    for i in range(n):  
        d += deliveries[i]  
        p += pickups[i]  

        while d > 0 or p > 0: #어딘가의 지점에 도착했다면
            d -= cap #음수가 되어도 다음 집에서 음수 크기만큼 작업량 save
            p -= cap 
            answer += (n - i) * 2 #끝에서부터 오니까 실제 거리 계산은 (n-i), 왕복하니까 2배
            
    return answer

# 안 뒤집고 풀려고 하니 시간초과 발생
# 배열 뒤집어서 푸는 부분 구글 참고했음