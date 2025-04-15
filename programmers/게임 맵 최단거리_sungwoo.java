// 풀이 시간: 17분

import java.util.*;

class Point {  // xy 좌표를 담는 클래스
    int x, y;
    Point(int x, int y) { this.x = x; this. y = y; }
}

class Solution {

    int[] dx = new int[] {1, -1, 0, 0};
    int[] dy = new int[] {0, 0, 1, -1};

    public boolean isValid(int x, int y, int[][] maps) {  // 이동할 수 있는 xy 좌표인지 검사
        if (x >= 0 && x < maps.length && y >= 0 && y < maps[0].length && maps[x][y] != 0)
            return true;
        return false;
    }

    public int solution(int[][] maps) {

        Queue<Point> q = new LinkedList<>();  // 큐 생성
        boolean[][] visited = new boolean[maps.length][maps[0].length];  // 방문 여부 불린 배열
        visited[0][0] = true;

        q.offer(new Point(0, 0));  // (0, 0)부터 BFS 탐색 시작

        while (!q.isEmpty()) {
            Point p = q.poll();

            for (int i = 0; i < 4; i++) {  // 상하좌우 탐색
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];

                if (isValid(nx, ny, maps) && !visited[nx][ny]) {
                    q.offer(new Point(nx, ny));
                    visited[nx][ny] = true;
                    maps[nx][ny] = maps[p.x][p.y] + 1;  // 현 위치의 원소값에 1을 더한 값으로 갱신 (초기값이 1이기 때문에 자연스럽게 칸의 개수로 갱신됨)
                }
            }
        }

        if (maps[maps.length - 1][maps[0].length - 1] > 1)  // 목적지의 원소 값이 1이 아닌 '칸의 최솟값'으로 갱신된 경우 해당 값 리턴
            return maps[maps.length - 1][maps[0].length - 1];

        return -1;  // 도달하지 못한 경우 -1 리턴
    }
}