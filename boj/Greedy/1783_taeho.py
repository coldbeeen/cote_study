import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 3*7 짜리 체스판 안에서는 4회까지는 자유롭게 이동

if N == 1:
    print(1)

# 2번 또는 3번밖에 못씀 => min(이동제약, 노가다 계산 공식)
elif N == 2:
    print(min(4, (M-1) // 2 + 1))

# 체스판 가로길이가 7일 때까지는
# 1234번 방법을 다 쓰면 최대 4칸이고,
# 이동제약 없이 맘대로 가면 1번 또는 4번만 사용해서 최대 M칸 감
# => min(이동제약, 지맘대로)
elif M <=6:
    print(min(4, M))

# 체스판 가로길이 7부터는 자유롭게 이동 가능한데, 
# 2번 또는 3번을 최소 1번 사용했을 때 각각 1번씩 손해보니까
# 가로길이 - 2
else:
    print(M-2)