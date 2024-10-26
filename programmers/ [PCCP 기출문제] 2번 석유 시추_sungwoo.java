import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;

class Solution {

    int[] dx = {1, -1, 0, 0};  // x, y 변화량 배열
    int[] dy = {0, 0, 1, -1};

    class Node {  // 큐의 원소로 사용할 노드
        public int x, y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public int[][] copy2dimArr(int[][] arr) {  // 2차원 배열 복사 함수
        int[][] copiedArr = new int[arr.length][arr[0].length];
        for (int i = 0; i < arr.length; i++)
            for (int j = 0; j < arr[0].length; j++)
                copiedArr[i][j] = arr[i][j];

        return copiedArr;
    }

    public void bfs(int[][] land, int x, int y, int[] colCnt) {  // bfs 함수 (석유 개수 리턴)
        int n = land.length, m = land[0].length;

        Queue<Node> q = new LinkedList<>();  // 큐 생성
        land[x][y] = 0;  // land에 0(빈 땅)을 표시하여 방문 여부를 표현
        HashSet<Integer> cols = new HashSet<>();  // 방문한 석유 위치의 열을 기록 (colCnt에 석유 개수를 누적하기 위함)

        q.offer(new Node(x, y));  // 시작 좌표 입력
        int cnt = 0;  // 석유 개수

        while (!q.isEmpty()) {  // 탐색 수행
            Node node = q.poll();
            x = node.x; y = node.y;
            cols.add(y);  // 석유의 열을 기록
            cnt++;  // 석유 개수 증가

            for (int i = 0; i < 4; i++) {  // 상하좌우 탐색
                int nx = x + dx[i], ny = y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && land[nx][ny] == 1) {  // 유효한 위치이고, 해당 위치가 석유(미방문)라면 방문
                    land[nx][ny] = 0;  // 방문 처리
                    q.offer(new Node(nx, ny));
                }
            }
        }

        for (int col : cols)  // colCnt의 방문한 열에 석유 개수 누적
            colCnt[col] += cnt;
    }

    public int solution(int[][] land) {
        int n = land.length, m = land[0].length;
        int[] colCnt = new int[m];  // 열 단위 석유 개수

        for (int c = 0; c < m; c++) {  // c열 시추 수행
            for (int r = 0; r < n; r++)  // c열의 모든 행에 대해 탐색
                if (land[r][c] == 1)  // 석유이며 미방문한 위치라면 탐색
                    bfs(land, r, c, colCnt);
        }

        return Arrays.stream(colCnt).max().getAsInt();
    }
}