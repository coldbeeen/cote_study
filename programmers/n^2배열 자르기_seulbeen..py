# 23분
# 처음에 부분합인가 하고 하다가 로직 못짜서 기각
# 밑에 주석처럼 규칙찾아서 2차원 배열 만들고 1차원 배열로 재생성했는데 시간초과

"""풀이: 2차원배열을 1차원으로 이어주면 배열의 인덱스는 당연히 2차원배열의 i행j열 인덱스의 합임
5x5배열이라고 가정하면
0 1 2 3 4/5 6 7 8 9/10 11 12 13 14/15~
규칙을 찾다보니까 행이 바뀜에 따라 n으로 나눴을때의 몫이 달라짐

1행은 i%5 +1(이건 인덱스가 0부터 시작해서 보정값)
2행은 789는 i%5 +1 , 6,7은 i//5 +1
3행은 10 11 12 까지는 나머지, 13 14는 몫이 더 큼
행이 바뀜에 따라 몫이 달라지고, 해당 인덱스에서 n으로 나눴을때의 몫과 나머지중 큰 쪽을 선택하고 인덱스 보정으로 1 추가해주면 딱 맞음

"""
def solution(n, left, right):
    answer = []
    # matrix=[[i for i in range(1,n+1)]for _ in range(n)]
    # for i in range(1,n):
    #     for j in range(i):
    #         matrix[i][j]=i+1
    # answer=[matrix[i][j] for i in range(n) for j in range(n)]
    for i in range(left, right + 1):
        answer.append(max(i % n, i // n) + 1)
    return answer
