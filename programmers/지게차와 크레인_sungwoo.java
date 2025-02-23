// 풀이 시간: 70분
// 풀이 방법: empty 배열 생성하여 컨테이너 존재 유무를 처리.
// 지게차의 경우, 모든 컨테이너를 순회하며 해당 컨테이너에서 외부로 향할 수 있는지 BFS를 수행함.

import java.util.*;

class Solution {

    class Point {  // 좌표 클래스
        int x, y;
        Point(int x, int y) { this.x = x;  this.y = y; }
    }

    int[] dx = {1, -1, 0, 0};  // 좌표 변화량
    int[] dy = {0, 0, 1, -1};

    public boolean bfs(boolean[][] empty, int x, int y, int N, int M) {  // 외부에서 접근 가능 여부(꺼낼 수 있는지)를 구하기 위한 BFS

        Queue<Point> q = new LinkedList<>();  // 큐
        boolean[][] visited = new boolean[N][M];  // 방문 여부
        boolean isPullable = false;  // 꺼낼 수 있는지 여부
        q.offer(new Point(x, y));  // (x, y)에서 시작

        while (!q.isEmpty()) {
            Point p = q.poll();

            for (int i = 0; i < 4; i++) {  // 상하좌우 확인

                int nx = p.x + dx[i], ny = p.y + dy[i];

                if (!(nx >= 0 && nx < N && ny >= 0 && ny < M))  {  // 외부에 도달했다면
                    return true;
                } else if (!visited[nx][ny] && empty[nx][ny] == true) {  // 비어있는 곳(컨테이너 없는 곳)이라면
                    q.offer(new Point(nx, ny));  // 이어서 탐색
                    visited[nx][ny] = true;  // 방문 처리
                }
            }
        }

        return false;
    }

    public int solution(String[] storage, String[] requests) {

        int N = storage.length, M = storage[0].length();
        char[][] storageArr = new char[N][M];  // 문자 배열

        for (int i = 0; i < N; i++)  // 문자열 -> 문자 배열
            storageArr[i] = storage[i].toCharArray();


        boolean[][] empty = new boolean[N][M];  // 컨테이너 비었는지 여부
        int containerCnt = N * M;  // 남은 컨테이너 수

        for (String request: requests) {  // 요청 순회

            char ch = request.charAt(0);

            if (request.length() == 1) {  // 지게차 사용

                ArrayList<Point> pulled = new ArrayList<>();  // 리스트 생성 (탐색 하는 동안 빼낼 컨테이너를 모아두고, Empty 배열 수정을 한 번에 처리해야 함)

                for (int i = 0; i < N; i++) {
                    for (int j = 0; j < M; j++) {
                        if (empty[i][j] == false && storageArr[i][j] == ch) {
                            boolean isPullable = bfs(empty, i, j, N, M);  // 지게차로 빼낼 수 있는지 BFS 탐색
                            if (isPullable)  // 빼낼 수 있다면 pulled 리스트에 추가
                                pulled.add(new Point(i, j));
                        }
                    }
                }

                for (Point p: pulled) {  // 빼낼 수 있는 컨테이너 모두 순회하며 empty 배열 true로 처리
                    empty[p.x][p.y] = true;
                    containerCnt--;
                }

            } else {  // 크레인 사용

                for (int i = 0; i < N; i++) {  // 해당 컨테이너 모두 꺼냄
                    for (int j = 0; j < M; j++) {
                        if (empty[i][j] == false && storageArr[i][j] == ch) {
                            empty[i][j] = true;
                            containerCnt--;
                        }
                    }
                }
            }
        }

        return containerCnt;
    }
}