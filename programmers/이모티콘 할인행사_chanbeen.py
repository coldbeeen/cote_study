def solution(users, emoticons):
    def make_candidates(array, idx):
        if idx == len(array):
            candidates.append(array[:])
            return
            
        for d in discounts:
            array[idx] += d
            make_candidates(array, idx + 1)
            array[idx] -= d #백트래킹
    
    discounts = [10, 20, 30, 40]
    candidates = []
    
    make_candidates([0] * len(emoticons), 0) #가능한 모든 할인율 조합 생성
    
    answer = [0, 0]
    
    for discount in candidates: #할인율 조합마다, 각 유저마다, 각 이모티콘에 해당하는 할인율마다 계산 (3중 반복)
        emoticon_plus_user = 0 #서비스 가입자
        profit = 0 #판매액
        
        for user in users:
            cost = 0 #유저별로 지출 비용 계산
            for i in range(len(discount)):
                if user[0] <= discount[i]: #유저별 특정 할인율 이상 시 할인된 가격에 이모티콘 구매
                    cost += emoticons[i] * (100 - discount[i]) / 100 
                
            if cost >= user[1]: #지출 비용이 임계값을 넘으면 이모티콘 플러스 가입
                cost = 0 #이모티콘 구매를 취소
                emoticon_plus_user += 1
            
            profit += cost
        
        if answer[0] <= emoticon_plus_user:
            if answer[0] == emoticon_plus_user: #2순위가 수익이므로 가입자가 같을 때 수익 비교
                answer[1] = max(answer[1], profit)
            else:
                answer[1] = profit
                
            answer[0] = emoticon_plus_user
                
    return answer

# 재귀함수를 활용하여 완전탐색으로 할인율을 이모티콘별로 다 조합해서 비용을 계산해봐야겠다고 판단
# candidates를 만드는 과정에서 array[:]가 아닌 array를 append하게 되면 array의 주소를 참조하는 것이라서 다른 재귀문에서 array의 값이 변경되면 candidates에 저장되어 있던 요소의 값도 같이 바뀌게 된다
# 할인율은 10, 20, 30, 40 중 하나이므로, 리스트로 생성해놓는 것이 편할 것 같다