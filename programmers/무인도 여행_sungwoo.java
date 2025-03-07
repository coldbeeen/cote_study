// 풀이 시간: 23분

import java.util.*;

class Solution {

    class Point {
        int x, y;
        Point(int x, int y)  { this.x = x; this.y = y; }
    }

    ArrayList<Integer> result = new ArrayList<>();
    int[] dx = {1, -1, 0, 0};
    int[] dy = {0, 0, 1, -1};

    public void getIslandFood(char[][] map, boolean[][] visited, Point start) {  // BFS 기반 식량 탐색

        int M = map.length, N = map[0].length, food = 0;

        Queue<Point> q = new LinkedList<>();  // BFS를 위한 큐 생성
        q.offer(start);  // 시작 지점
        visited[start.x][start.y] = true;

        while (!q.isEmpty()) {  // 큐가 빌 때까지 반복

            Point p = q.poll();
            food += map[p.x][p.y] - '0';  // 무인도 식량 누적

            for (int i = 0; i < 4; i++) {

                int nx = p.x + dx[i];
                int ny = p.y + dy[i];

                if (nx >= 0 && nx < M && ny >= 0 && ny < N && map[nx][ny] != 'X' && !visited[nx][ny]) {  // 유효한 위치이고 바다가 아니며 방문하지 않았다면
                    q.offer(new Point(nx, ny));  // 큐에 삽입
                    visited[nx][ny] = true;
                }
            }
        }

        result.add(food);  // 최종 식량을 result에 삽입
    }

    public int[] solution(String[] maps) {

        int M = maps.length, N = maps[0].length();
        char[][] map = new char[M][N];
        boolean[][] visited = new boolean[M][N];

        for(int i = 0; i < M; i++)  // 2차원 char Array로 변환
            map[i] = maps[i].toCharArray();

        for (int i = 0; i < M; i++)
            for (int j = 0; j < N; j++)
                if (map[i][j] != 'X' && !visited[i][j])  // 바다가 아니며 방문하지 않았다면
                    getIslandFood(map, visited, new Point(i, j));  // 무인도 BFS 수행

        if (result.isEmpty())  // 지낼 수 있는 무인도가 없다면 -1 리턴
            return new int[] {-1};

        Collections.sort(result);  // 정렬 후 배열로 변환해 리턴
        return result.stream().mapToInt(i -> i).toArray();
    }
}