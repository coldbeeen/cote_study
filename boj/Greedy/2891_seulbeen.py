# ㅅ발 구글링함 이 코드도 결국 중간원소일때 자기 앞팀부터 빌려주는데 어떻게 최적해가 나오는지 모르겠음
n, s, r = map(int, input().split())

demaged = list(map(int,input().split()))
extra = list(map(int,input().split()))

# 카약 정보를 가지는 리스트 생성 후 1으로 초기화
c = [1] * n

# 손상된 카약을 가진 팀 = 0 
for i in demaged:
    c[i-1] -= 1

# 여분의 카약을 가진 팀 = 2
for i in extra:
    c[i-1] += 1

for i in range(len(c)):
    # 손상된 카약을 가진 팀이라면
    if c[i] == 0:
        # 첫번째 원소일때
        if i == 0:
            if c[i+1] == 2:
                c[i+1] = 1
                c[i] = 1
        # 마지막 원소일때
        elif i == len(c)-1:
            if c[i-1] == 2:
                c[i-1] = 1
                c[i] = 1
        # 중간 원소일때
        else:
            if c[i-1] == 2:
                c[i-1] = 1
                c[i] = 1
                continue              
            if c[i+1] == 2:
                c[i+1] = 1
                c[i] = 1
                continue
print(c.count(0)) # count 메소드 쓰면 대네