// 풀이 시간: 29분 (와 찢었다)
// 풀이 방법: 모든 경우의 수를 고려하는 것은 시간복잡도가 너무 커질 것이라 생각했고,
//            다익스트라 알고리즘(최단 경로)을 변형해서 풀어볼 수 있을까? 하고 접근했다.
//            거리를 비용으로 설정하는 것이 아닌, 부숴야하는 벽을 비용으로 설정해 이를 최소화하도록 알고리즘을 구현하였다.

import java.io.*;
import java.util.*;

public class Main {

    static class Point {  // x, y, destroyCount를 갖는 클래스

        int x, y, destroyCount;

        Point (int x, int y, int destroyCount) {
            this.x = x;
            this.y = y;
            this.destroyCount = destroyCount;
        }
    }

    public static final int[] dx = {1, -1, 0, 0};  // x와 y의 변위 배열
    public static final int[] dy = {0, 0, 1, -1};

    public static int dijkstra(int[][] graph, int N, int M) {  // 부술 벽의 개수를 최소화하는 다익스트라 알고리즘 (최소 비용 리턴)

        PriorityQueue<Point> pq = new PriorityQueue<>((a, b) -> Integer.compare(a.destroyCount, b.destroyCount));  // 부술 벽을 기준으로 최소힙 생성
        pq.offer(new Point(0, 0, 0));  // 초기 위치 설정

        int[][] destroyCountGraph = new int[N][M];  // 부술 벽 개수(비용) 배열 설정 (N + M으로 초기화)
        for (int i = 0; i < N; i++)
            Arrays.fill(destroyCountGraph[i], N + M);
        destroyCountGraph[0][0] = 0;

        while (!pq.isEmpty()) {  // 힙이 빌 때까지 반복

            Point point = pq.poll();

            for (int i = 0; i < 4; i++) {  // 상하좌우 고려

                int nx = point.x + dx[i];
                int ny = point.y + dy[i];

                if (nx >= 0 && nx < N && ny >= 0 && ny < M) {

                    int toDestroy = graph[nx][ny] == 0 ? 0 : 1;  // 벽이라면 toDestroy를 1로 설정

                    if (point.destroyCount + toDestroy < destroyCountGraph[nx][ny]) {  // destroyCount + toDestroy가 기존 배열 값보다 작다면 갱신 후 힙에 삽입
                        destroyCountGraph[nx][ny] = point.destroyCount + toDestroy;
                        pq.offer(new Point(nx, ny, destroyCountGraph[nx][ny]));
                    }
                }
            }
        }

        return destroyCountGraph[N - 1][M - 1];
    }

    public static void main(String[] args) throws Exception {

        // 0. 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] s1 = br.readLine().split(" ");
        final int M = Integer.parseInt(s1[0]), N = Integer.parseInt(s1[1]);

        int[][] graph = new int[N][M];

        for (int i = 0; i < N; i++) {
            String s2 = br.readLine();
            for (int j = 0; j < M; j++)
                graph[i][j] = Character.getNumericValue(s2.charAt(j));
        }

        // 1. 부숴야하는 벽을 기준으로 다익스트라 수행
        System.out.println(dijkstra(graph, N, M));

    }
}