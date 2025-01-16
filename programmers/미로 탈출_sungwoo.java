// 풀이 시간: 45분

import java.util.*;

class Solution {

    class Node {  // 좌표와 비용(시간)을 담는 클래스
        int x; int y;
        int cost;
        Node(int x, int y, int cost) {
            this.x = x; this.y = y; this.cost = cost;
        }
    }

    public int mazeSearch(char[][] maps) {  // BFS 수행 메서드

        int M = maps.length; int N = maps[0].length;  // 가로/세로 크기
        boolean[][] visited = new boolean[M][N];  // 방문 여부 확인용 배열
        int[] dx = {1, -1, 0, 0};  // x, y 변화량
        int[] dy = {0, 0, 1, -1};

        // 1. find (x, y) of start, lever, end
        int startX = -1, startY = -1; int leverX = -1, leverY = -1; int endX = -1, endY = -1;

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (maps[i][j] == 'S') {  // start point
                    startX = i; startY = j;
                } else if (maps[i][j] == 'L') {  // lever point
                    leverX = i; leverY = j;
                } else if (maps[i][j] == 'E') {  // end point
                    endX = i; endY = j;
                }
            }
        }

        // 2. set up queue
        Queue<Node> q = new LinkedList<>();  // 큐 생성
        q.offer(new Node(startX, startY, 0));  // 시작점 삽입
        visited[startX][startY] = true;  // 시작점 방문 체크
        boolean leverVisit = false;  // 레버 방문 여부 (레버 방문 및 end 도달 시 종료하기 위함)
        int cost = -1;

        // 3. bfs
        while(!q.isEmpty()) {

            Node curNode = q.poll();

            if (curNode.x == leverX && curNode.y == leverY) {  // 레버에 도달했다면, queue와 visited 초기화 후 end를 향해 이어서 탐색
                visited = new boolean[M][N];
                visited[leverX][leverY] = true;
                q.clear();
                leverVisit = true;  // 레버 방문 체크
            }

            if (leverVisit && curNode.x == endX && curNode.y == endY) {  // 출구
                cost = curNode.cost;
                break;
            }

            for(int i = 0; i < 4; i++) {  // 상하좌우 방향 탐색
                int nx = curNode.x + dx[i];
                int ny = curNode.y + dy[i];

                if (nx >= 0 && nx < M && ny >= 0 && ny < N && maps[nx][ny] != 'X' && !visited[nx][ny]) {  // 위치 유효성 및 방문 여부 검사
                    q.offer(new Node(nx, ny, curNode.cost + 1));
                    visited[nx][ny] = true;
                }
            }
        }

        return cost;
    }

    public int solution(String[] maps) {
        char[][] charMaps = new char[maps.length][];

        for (int i = 0; i < maps.length; i++)  // char[][]로 변환 수행
            charMaps[i] = maps[i].toCharArray();

        return mazeSearch(charMaps);  // BFS 수행 및 결과 리턴
    }
}