// 풀이 시간: 30분
// 풀이 방법: 모든 좌표에서 상하좌우 방향으로의 길을 visited(방문 여부 배열)에 표시함으로서 문제를 풀어나갔음 (3차원 배열 사용). 탐색을 수행하면서 visited를 활용해 문제를 해결할 수 있었음.

import java.util.*;

class Solution {

    HashMap<Character, Integer> dirMap = new HashMap<>();
    int[] dx = {-1, 0, 1, 0};
    int[] dy = {0, -1, 0, 1};

    public Solution() {  // dirMap 초기화를 위한 생성자
        char[] dir = {'L', 'D', 'R', 'U'};
        for (int i = 0; i < 4; i++)
            dirMap.put(dir[i], i);
    }

    public int searchPath(String dirs) {

        boolean[][][] visited = new boolean[11][11][4];

        int x = 5, y = 5;  // 시작 위치
        int result = 0;  // 처음 방문한 길의 길이 (answer)

        for (char dir: dirs.toCharArray()) {  // dirs를 순회함

            int dirVal = dirMap.get(dir);  // 방향 'char' -> 'int'로 매핑

            int nx = x + dx[dirVal];
            int ny = y + dy[dirVal];

            if (!(nx >= 0 && nx < 11 && ny >= 0 && ny < 11))  // 이동하려는 위치가 유효한지
                continue;

            if (!visited[x][y][dirVal]) {  // 해당 위치에서 dir 방향의 길을 방문하지 않았다면
                visited[x][y][dirVal] = true;  // 해당 위치에서 dir 방향으로의 길 방문 표시
                visited[nx][ny][(dirVal + 2) % 4] = true;  // 이동하려는 위치에서 dir 반대방향으로의 길도 방문 표시
                result++;
            }
            x = nx;
            y = ny;
        }
        return result;
    }

    public int solution(String dirs) {
        int answer = searchPath(dirs);
        return answer;
    }
}