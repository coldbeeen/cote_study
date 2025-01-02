# 1900-35분 ㄷ
# 먼저 무적권을 다 소모해서 가장 병사가 많은 라운드에 사용해줬는데 시간초과 및 오답이 많았음
# 무적권을 미리 쓰지 말고 라운드를 진행하다가 라운드 진행이 안되면 무적권을 뒤늦게 사용해서 사실 그때 사용한척 하자
# 뒤늦게 사용할 때 이미 진행한 라운드중 가장 병사가 많았던 라운드에 사용하면 됨
import heapq


def solution(n, k, enemy):
    answer = 0
    #     for i in range(k):
    #         idx=enemy.index(max(enemy))
    #         enemy[idx]=0
    killed_enemy = []

    for i in range(len(enemy)):
        if n >= enemy[i]:
            n -= enemy[i]
            heapq.heappush(killed_enemy, -enemy[i])
        else:
            if k > 0:
                if -killed_enemy[0] < enemy[i]:
                    tmp = heapq.heappop(killed_enemy)
                    k -= 1
                    n += -tmp
                    n -= enemy[i]
                    heapq.heappush(killed_enemy, -enemy[i])
                else:
                    k -= 1
                    heapq.heappush(killed_enemy, -enemy[i])
            else:
                return answer
        answer += 1
    return min(answer, len(enemy))


n=int(input())
k=int(input())
tmp=input().split(" ")
enemy=[int(t) for t in tmp]
print(solution(n,k,enemy))
