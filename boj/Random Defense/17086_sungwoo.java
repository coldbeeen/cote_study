import java.io.*;
import java.util.*;

public class Main
{

    public static final int[] dx = {0, 0, 1, -1, -1, -1, 1, 1};
    public static final int[] dy = {1, -1, 0, 0, -1, 1, -1, 1};
    public static final int MAX = Integer.MAX_VALUE;

    public static int bfs(int[][] graph, int N, int M) {

        int[][] cost = new int[N][M];  // cost 배열 초기화
        for (int i = 0; i < N; i++)
            Arrays.fill(cost[i], MAX);

        Queue<int[]> q = new LinkedList<>();  // 큐 생성 및 상어 위치 좌표 삽입
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (graph[i][j] == 1) {
                    cost[i][j] = 0;
                    q.offer(new int[] {i, j});
                }
            }
        }

        while (!q.isEmpty()) {  // BFS 수행

            int[] xy = q.poll();
            int curX = xy[0], curY = xy[1];

            for (int i = 0; i < 8; i++) {  // 8개의 방향 확인
                int nx = curX + dx[i];
                int ny = curY + dy[i];

                if (nx >= 0 && nx < N && ny >= 0 && ny < M && cost[nx][ny] == MAX) {  // 방문하지 않은 유효한 위치라면
                    q.offer(new int[] {nx, ny});
                    cost[nx][ny] = cost[curX][curY] + 1;
                }
            }
        }

        int max = 0;
        for (int i = 0; i < N; i++)  // 최댓값 계산
            for (int j = 0; j < M; j++)
                if (cost[i][j] > max)
                    max = cost[i][j];

        return max;

    }


    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()), M = Integer.parseInt(st.nextToken());
        int[][] graph = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++)
                graph[i][j] = Integer.parseInt(st.nextToken());
        }

        System.out.println(bfs(graph, N, M));  // 다익스트라 메서드 호출
    }
}