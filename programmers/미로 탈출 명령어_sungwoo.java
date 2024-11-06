import java.util.*;

class Solution {

    int[] dx = {1, 0, 0, -1};  // x, y 변화량 배열
    int[] dy = {0, -1, 1, 0};
    char[] direction = {'d', 'l', 'r', 'u'};  // 위 변화량에 대한 방향 배열 (사전순으로 가장 빠른 경로를 찾기 위해 사전순으로 생성)

    class Point {  // x, y 좌표 저장
        int x, y;
        Point(int x, int y) { this.x = x; this.y = y; }
    }

    class Path {  // 좌표와 경로(String) 저장
        Point point;
        String pathString;

        Path(Point point, String pathString) {
            this.point = point; this.pathString = pathString;
        }
    }

    public String solution(int n, int m, int x, int y, int r, int c, int k) {

        String answer = "impossible";

        Queue<Path> q = new LinkedList<>();  // 큐 생성 및 시작 지점에 대한 원소 삽입
        Path start = new Path(new Point(x - 1, y - 1), "");
        q.offer(start);

        while (!q.isEmpty()) {  // BFS 수행
            Path path = q.poll();
            int cx = path.point.x, cy = path.point.y;
            String pathString = path.pathString;

            if (pathString.length() == k) {  // 경로 String의 길이가 k에 도달하면 도착 지점에 위치한지 검사
                if (cx == r - 1 && cy == c - 1) {
                    answer = pathString;  // 정답을 찾았다면 탐색 종료 (사전순으로 탐색을 진행하기 때문에 바로 종료함)
                    break;
                }
                continue;
            }

            for(int i = 0; i < 4; i++) {  // 상하좌우 탐색
                int nx = cx + dx[i], ny = cy + dy[i];
                int distanceToDestination = Math.abs(r - 1 - nx) + Math.abs(c - 1 - ny);  // 남은 거리
                int remainingStep = k - pathString.length() - 1;  // 남은 이동 횟수

                if ((nx >= 0 && nx < n) && (ny >= 0 && ny < m)  // 범위를 벗어나지 않고, 남은 거리가 step을 초과하지 않는다면, 큐에 삽입
                        && distanceToDestination <= remainingStep && (remainingStep - distanceToDestination) % 2 == 0) {
                    Path newPath = new Path(new Point(nx, ny), pathString + direction[i]);
                    q.offer(newPath);
                    break;  // 사전순으로 빠른 경로를 찾기 때문에 나머지 경우의 수는 고려하지 않고 break
                }
            }
        }

        return answer;
    }
}