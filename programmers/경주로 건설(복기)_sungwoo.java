// 풀이 시간: 70분 (이전 풀이 참고)

import java.util.*;

class Solution {

    class Point {  // 좌표, 방향, 비용을 담는 클래스
        int x, y, d, c;
        Point (int x, int y, int d, int c) {
            this.x = x; this.y = y; this.d = d; this.c = c;
        }
    }

    int[] dx = new int[] {1, -1, 0, 0};
    int[] dy = new int[] {0, 0, 1, -1};

    public int solution(int[][] board) {

        int r = board.length, c = board[0].length;
        int[][][] cost = new int[r][c][4];  // 비용을 담을 3차원 리스트 (좌표와 방향에 따른 cost)

        for (int i = 0; i < r; i++)  // 비용 리스트 초기화
            for (int j = 0; j < c; j++)
                Arrays.fill(cost[i][j], Integer.MAX_VALUE);


        Queue<Point> queue = new LinkedList<>();  // BFS를 위한 큐 생성
        queue.offer(new Point(0, 0, 0, 0));

        while (!queue.isEmpty()) {  // BFS 시작

            Point point = queue.poll();

            if (point.x == r - 1 && point.y == c - 1)  // 목적지 도착
                continue;

            for (int i = 0; i < 4; i++) {  // 상하좌우 진행

                int nx = point.x + dx[i];  // 다음 위치 계산
                int ny = point.y + dy[i];

                if (nx >= 0 && nx < r && ny >= 0 && ny < c && board[nx][ny] == 0) {  // 유효한 위치라면 비용 계산
                    // point가 시작 지점이거나 진행하려는 방향이 같으면 100, 아니면 600을 더함
                    int curCost = point.c + (point.d == i || point.x + point.y == 0 ? 100 : 600);

                    if (curCost >= cost[nx][ny][i])  // 더 적은 비용이 아니라면 건너뜀
                        continue;

                    cost[nx][ny][i] = curCost;  // 비용 배열 갱신
                    queue.offer(new Point(nx, ny, i, curCost));  // 큐에 추가
                }
            }

        }

        return Arrays.stream(cost[r-1][c-1]).min().getAsInt();  // 목적지 비용에서 최솟값을 구함
    }
}