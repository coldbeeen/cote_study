import pandas as pd

def solution(friends, gifts):
    answer = 0
    
    score = {} #선물 지수
    next_month = {} #다음달 선물 계산
    
    df = pd.DataFrame(index = friends) #누가, 누구에게 몇 개 줬는지 계산용 df
    
    for f in friends:
        score[f] = 0
        next_month[f] = 0
        df[f] = 0
    
    for g in gifts:
        source, dest = g.split(' ')
        score[source] += 1
        score[dest] -= 1 
        df.loc[source][dest] += 1
    
    for i in friends:
        for j in friends:
            if i != j:
                if df.loc[i][j] > df.loc[j][i]:
                    next_month[i] += 1
                elif df.loc[i][j] < df.loc[j][i]:
                    next_month[j] += 1
                else:
                    if score[i] > score[j]:
                        next_month[i] += 1
                    elif score[i] < score[j]:
                        next_month[j] += 1
                    
    answer = (max(next_month.values())) // 2 #모든 행과 열을 돌면서 2번씩 계산되었으므로, 2로 나눔
    
    return answer

# 단순 구현 문제
# 의식의 흐름대로 풀다 보니 판다스를 썼는데.. 잘 풀었다고는 생각되지 않음
# 변수를 너무 많이 선언한 느낌

# Lv1인데 정답률 24%라서 골라봤는데 이유를 잘 모르겠다