# 0인 인덱스를 모아놓는 것은 유지하되, 슬라이딩 윈도우로 시간복잡도를 아끼자
import ast

def solution(cylinder, a):
    result = []
    mo = 0
    ja = 0
    n = len(cylinder)
    no_bullet = list(filter(lambda x: cylinder[x] == 0, range(len(cylinder))))
    
    # 총알을 발사할 수 있는지 확인 하는 함수
    def can_balssa(start,end):
        if start==end:
            if cylinder[start]==1:
                return False
            return True
        
        while start!=end:
            if cylinder[start]==1:
                return False
            start=(start+1)%n
        return True
    
    #0번 인덱스에 대해 미리 계산
    l=(no_bullet[0]+1)%n
    r=(no_bullet[0]+a)%n
    flag=can_balssa(l,r)
    mo+=1
    if flag:
        ja+=1
    
    
    #그 다음 인덱스부터 계산
    for idx in no_bullet[1:]:
        l=(idx+1)%n
        r = (idx + a) % n
        mo+=1
        # 이전에 총알이 있었다면 다시 계산
        if not flag:
            flag=can_balssa(l,r)
        
        # 이전에 발사 성공을 했다는것=> 총알이 범위내에 1개도 없었다는 것
        else:
            # 갱신된 r에 해당하는 인덱스에 총알이있다면 False
            if cylinder[r]==1:
                flag=False
            #아니라면 총알이 또 없는것
            else:
                flag=True
                ja+=1

    # 기약분수화 파트
    if ja==0:
        return[0,1]
    for i in range(min(mo, ja), 1, -1):
        if mo % i == 0 and ja % i == 0:
            mo //= i
            ja //= i
            break
    result.append(ja)
    result.append(mo)

    return result


cylinder = input()
cylinder = ast.literal_eval(cylinder)
a = 4
# print(cylinder[0])
output = solution(cylinder, a)
print(output)
