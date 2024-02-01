import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    apply = [list(map(int, input().split())) for i in range(N)]
    
    apply.sort(key = lambda x : (x[0])) #서류심사 성적 순 정렬
    
    cnt = 0
    tmp = apply[0]
    for a in apply:
        if tmp[0] < a[0] and tmp[1] < a[1] : #서류심사와 면접시험 중 하나도 뛰어난 게 없는 지원자
            cnt += 1 #카운트
        else:
            tmp = a
    
    print(len(apply) - cnt) #카운트된 만큼 지원자 리스트에 반영