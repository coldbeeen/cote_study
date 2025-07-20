// 풀이 시간: DFS 25분 시도 → 시간 초과
//            다익스트라 25분

import java.util.*;
import java.io.*;

public class Main {

    public static class Point {  // 좌표와 도둑 루피를 담는 클래스
        int x; int y; int cost;
        public Point(int x, int y, int cost) {
            this.x = x; this.y = y; this.cost = cost;
        }
    }

    public static int[] dx = new int[] {1, -1, 0, 0};
    public static int[] dy = new int[] {0, 0, 1, -1};

    public static int dijkstra(int[][] graph, int N) {  // 다익스트라 수행

        PriorityQueue<Point> pq = new PriorityQueue<>((a, b) -> Integer.compare(a.cost, b.cost));  // 힙 생성
        pq.offer(new Point(0, 0, graph[0][0]));

        int[][] costArr = new int[N][N];  // 좌표까지의 최소 도둑 루피를 담을 배열
        for (int i = 0; i < N; i++)
            Arrays.fill(costArr[i], 1_000_000);

        while (!pq.isEmpty()) {

            Point point = pq.poll();
            int x = point.x, y = point.y, cost = point.cost;

            for (int i = 0; i < 4; i++) {  // 상하좌우 고려
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 0 && nx < N && ny >= 0 && ny < N && cost + graph[nx][ny] < costArr[nx][ny]) {  // 해당 좌표 진행이 최솟값일 때
                    costArr[nx][ny] = cost + graph[nx][ny];  // 최솟값 갱신
                    pq.offer(new Point(nx, ny, costArr[nx][ny]));  // 힙에 삽입
                }
            }
        }

        return costArr[N - 1][N - 1];  // 목적지까지의 최솟값 리턴
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int k = 1; ; k++) {

            int N = Integer.parseInt(br.readLine());

            if (N == 0)
                break;

            int[][] graph = new int[N][N];

            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++)
                    graph[i][j] = Integer.parseInt(st.nextToken());
            }

            System.out.printf("Problem %d: %d\n", k, dijkstra(graph, N));
        }
    }
}