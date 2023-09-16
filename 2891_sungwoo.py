import sys

N, S, R = map(int, sys.stdin.readline().split())  # N: 팀의 수, S: 카약 손상된 팀 수, R: 여분 카약 팀 수

S_list = list(map(int, sys.stdin.readline().split()))
R_list = list(map(int, sys.stdin.readline().split()))

S_list.sort()
R_list.sort()

S_idx = 0  # 카약 손상된 팀 인덱스
R_idx = 0  # 여분 카약 팀 인덱스

# 여분 카약 팀 순회 (여분 팀으로 순회를 돌면서 손상된 팀을 하나씩 메꿔주면서 진행하면 아직 손상되어 출발하지 못하는 팀을 구할 수 있다)
while R_idx < len(R_list) and S_idx < len(S_list):  # 요소가 제거되므로 항상 인덱스 크기를 길이와 비교하여 검사

    if R_list[R_idx]-1 <= S_list[S_idx] <= R_list[R_idx]+1:  # 여분 카약을 사용하는 조건. 손상팀과 여분팀을 리스트에서 제거
        if R_list[R_idx]-1 == S_list[S_idx] and S_idx < len(S_list)-1 and S_list[S_idx+1] == R_list[R_idx]:  # 자기 팀이 사용하는 경우 1 (아래 예시 참고)
            del R_list[R_idx]
            del S_list[S_idx+1]
        elif R_list[R_idx]+1 == S_list[S_idx] and R_idx < len(R_list)-1 and S_list[S_idx] == R_list[R_idx+1]:  # 자기 팀이 사용하는 경우 2
            del R_list[R_idx+1]
            del S_list[S_idx]
        else:  # 카약 빌려주기
            del S_list[S_idx]
            del R_list[R_idx]

    else:  # S, R 중 더 작은 값의 인덱스를 증가시킴
        if S_list[S_idx] < R_list[R_idx]:
            S_idx += 1
        else:
            R_idx += 1

print(len(S_list))


'''
10 5 2
1 2 3 6 7
7 8


10 5 2
1 2 3 6 7
7 8
'''