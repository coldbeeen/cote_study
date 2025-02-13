#약 73분 소요, 11 ~ 19번째 코드는 구글링한 코드로 대체

def solution(picks, minerals):
    answer = 0
    
    able_mineral = 5 * sum(picks) #한 곡괭이당 5개 캐기 가능
    
    if len(minerals) > able_mineral:
        minerals = minerals[:able_mineral] #캘 수 있는만큼 슬라이싱

    new_minerals = [[0, 0, 0] for _ in range(len(minerals) // 5 + 1)] #5개씩 끊어서 종류별로 카운트
    
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            new_minerals[i // 5][0] += 1
        elif minerals[i] == 'iron':
            new_minerals[i // 5][1] += 1
        elif minerals[i] == 'stone':
            new_minerals[i // 5][2] += 1
            
    new_minerals = sorted(new_minerals, key = lambda x : (-x[0], -x[1], -x[2])) #다이아, 철, 돌 내림차순 정렬
    
    print(new_minerals)
    
    for m in new_minerals:
        dia, iron, stone = m #종류별 광물 개수
        
        for i in range(len(picks)): #다이아 -> 철 -> 돌 순서로 많은 광물 조합이 우선적으로 등장함
            if i == 0 and picks[i] > 0: #다이아 곡괭이
                answer += dia + iron + stone
                picks[i] -= 1
                break #break 안 하면 다른 곡괭이 조건문으로 진입함
                
            elif i == 1 and picks[i] > 0: #철 곡괭이
                answer += 5 * dia + iron + stone
                picks[i] -= 1
                break
                
            elif i == 2 and picks[i] > 0: #돌 곡괭이
                answer += 25 * dia + 5 * iron + stone
                picks[i] -= 1
                break
                
    return answer

#광물은 주어진 순서대로만 캘 수 있음
#곡괭이는 종류 상관없이 광물 5개 캔 후 사용 불가, 한 번 선택하면 사용 불가 상태까지 써야함
#곡괭이는 종류별로 5개 이하
#광물 배열 길이 제한 50 -> 복잡도가 높은 알고리즘도 괜찮다
#곡괭이가 없거나 모든 광물 캘 때까지 반복 
#한 번 고르면 5번 써야하므로, 5개씩 광물을 끊은 뒤 최대한 효율적으로 곡괭이 사용
#다이아가 가장 많으면 다이아 곡괭이 사용하는 방식
#광물을 5개씩 끊어서 새로운 2차원 리스트로 만들어주고, (다이아, 철, 돌)을 key로 하여 내림차순 정렬 
#이후 곡괭이 개수 줄여가며 표대로 피로도 계산



#     new_minerals = []
#     minerals_cnt = [0, 0, 0]
#     idx = 0
    
#     for i in range(len(minerals)):
#         if minerals[i] == 'diamond':
#             minerals_cnt[0] += 1
#         elif minerals[i] == 'iron':
#             minerals_cnt[1] += 1
#         elif minerals[i] == 'stone':
#             minerals_cnt[2] += 1
        
#         idx += 1

#         if idx == 5 or i == len(minerals) - 1:
#             new_minerals.append(minerals_cnt)
#             minerals_cnt = [0, 0, 0]
#             idx = 0