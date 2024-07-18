# dfs를 통해 해결한 문제
#
# 몇가지 경우의 수가 있는지를 물어보는 문제이므로 모든 경우를 찾아야 한다. 모든 경우를 탐색할 때는 dfs 알고리즘을 선호해서 dfs를 통해 문제를 해결했다.
#
# 탐색하면서 uesr_id와 banned_id가 일치하는지 확인하고 일치한 갯수가 banned_id의 lengh와 같다면 즉 banned_id와 일치한 user_id를 모두 찾았다면 set에 찾은 user_id를 저장한다.
# set을 사용한 이유는 모든 경우를 찾기 때문에 중복한 경우가 있을 수 있기 때문이다. (문제 조건이 순서는 다르고 이름이 같다면 같은 경우라고 주어졌다.)
#
# 마지막으로 set의 길이를 return 해줌으로서 정답을 구할 수 있다.

def solution(user_id, banned_id):

    # 단일 user_id와 단일 banned_id를 입력받아 제재 사용자인지 검증함
    def check_condition(user_id, banned_id):

        # 문자열 길이가 다르다면 False
        if len(user_id) != len(banned_id):
            return False

        for i in range(len(user_id)):
            if user_id[i] != banned_id[i] and banned_id[i] != '*':
                return False

        return True

    # dfs를 수행하여 모든 경우의 수를 탐색함
    def dfs(step):

         # 경우의 수가 완성되면 방문한 아이디를 조합해 answer에 추가함
        if step == len(banned_id):
            tmp_list = []
            for i in range(len(visited)):
                if visited[i]:
                    tmp_list.append(user_id[i])

            answer.add(tuple(tmp_list))
            return

        # 모든 user_id를 순회하며, 1. 방문하지 않았고, 2. banned_id[step]에 해당하는 제재 아이디라면 이어서 DFS 수행 (백트래킹의 일종)
        for i in range(len(user_id)):
            if not visited[i] and check_condition(user_id[i], banned_id[step]):
                visited[i] = True
                dfs(step + 1)
                visited[i] = False

    answer = set()  # 중복되는 경우의 수를 제거하기 위함
    visited = [False for _ in range(len(user_id))]  # 아이디 방문 여부 리스트

    dfs(0)  # DFS 수행
    return len(answer)  # answer의 길이 리턴

u, b = ["aa", "ab", "ac", "ad", "ae", "be"], ["a*", "a*", "*e", "**"]
print(solution(u, b))