#약 53분 소요

import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())

length = int(input())
requests = [list(map(int, input().split())) for _ in range(length)]

result = []
user_dict = {}

for r in requests:
    time, id = r   
    print(f'current requested id : {id}')
    
    keys_to_delete = [] #최근 활동 후 b초 지난 id 삭제 목적 리스트
    
    for key, value in user_dict.items(): #활동 상태 갱신
        last_active, status = value
        
        if time - last_active >= a: #자리비움 업데이트
            user_dict[key] = [last_active, 0] #활동 상태) 1 : 활동 중, 0 : 자리비움
        
        if time - last_active >= b: #접속해제 처리
            keys_to_delete.append(key)
    
    for key in keys_to_delete: #최근 활동 후 b초 지난 id 접속해제
        del user_dict[key] 
    
    num_users = len(user_dict.keys()) #활동 상태 갱신 후 접속 유지 중인 유저 수
    
    if id in user_dict: #이미 접속해있는 유저
        user_dict[id] = [time, 1] #최근 활동 시간 갱신
        result.append(num_users)
        
        print("id already exist")
        print('-------------')
        
    else: #새로 접속하려는 유저
        
        print(f"id didn't exist, num_users : {num_users}")
        
        if num_users < n: #n명 미만, 바로 접속 accept
            user_dict[id] = [time, 1]
            result.append(len(user_dict.keys())) #접속 중인 유저 수 업데이트 됨, 반영
            print("new user joined")
            print('-------------')
        elif num_users == n:
            user_to_delete = 0
            min_active = 1e9 #최근 활동 시간이 가장 오래된 유저 탐색 목적 변수
            
            for key, value in user_dict.items():
                last_active, status = value
                
                if not status: #자리비움 상태인 유저 중
                    if min_active > last_active:
                        user_to_delete = key #가장 오래 자리비움한 유저 선별
                        min_active = last_active
            
            print(f'user_to_delete : {user_to_delete}')
            
            if not user_to_delete: #자리비움 중인 유저 x
                result.append(-1)
                
                print("no absence users")
                print('-------------')
            else:
                del user_dict[user_to_delete] #가장 오래 자리비움한 유저 접속해제
                
                user_dict[id] = [time, 1] #새 유저 접속
                result.append(num_users) #전체 유저 수는 변화 x
                
                print("new user joined after filtering")
                print('-------------')
            
print(f'result : {result}')
            
#[시간, id]로 이루어진 2차원 request배열
#a초 지나면 자리비움, b초 지나면 접속해제
#n명 미만일 때는 바로 접속
#n명일때는 가장 오래 자리비움한 id 접속해제 이후 접속
#요청 처리한 시점에서 몇 명이 접속 중인지 result에 값 저장
#자리비움 중인 id가 없다면 접속 거부, result에 -1 저장

#사람 수가 n명 미만이고 새로운 id가 등장했다면 바로 추가
#딕셔너리에는 id : [최근 활동 시간, 활동 상태]의 형태로 저장
#새로운 요청을 받을 때마다 id별 활동 상태를 갱신해줘야 함
#활동 상태) 1 : 활동 중, 0 : 자리비움(최근 활동 이후로 a초 경과) 
#입력받은 time과 id의 마지막 활동 시간을 비교해서 a 또는 b보다 길다면 자리비움 또는 접속해제

#입력 예시
# 5
# 100 200
# 7
# 11 1
# 12 2
# 13 1
# 16 3
# 200 1
# 214 1
# 216 1

# 2
# 10 100
# 8
# 2 1000
# 3 1001
# 4 1005
# 8 1000
# 12 1002
# 13 1002
# 14 1001
# 200 1301