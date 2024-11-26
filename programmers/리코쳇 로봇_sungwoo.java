// 풀이 시간: 44분

import java.util.*;

class Solution {

    int[] dx = {1, -1, 0, 0};
    int[] dy = {0, 0, 1, -1};

    class Node {  // x, y 좌표 및 이동 횟수를 가지는 클래스 (BFS 수행을 위한 Queue의 제네릭 타입으로 사용)
        int x, y, move;
        Node(int x, int y, int move) {this.x = x; this.y = y; this.move = move;}
    }

    public Node slide(char[][] board, Node node, int direction) {  // 벽이나 장애물을 만날 때까리 슬라이딩 수행

        int n = board.length, m = board[0].length;
        int x = node.x, y = node.y, move = node.move;

        while ((x + dx[direction] >= 0 && x + dx[direction] < n)  // 다음 위치가 벽 혹은 장애물일 때까지 direction 방향으로 이동
                && (y + dy[direction] >= 0 && y + dy[direction] < m)
                && board[x + dx[direction]][y + dy[direction]] != 'D') {
            x += dx[direction];
            y += dy[direction];
        }
        return new Node(x, y, move + 1);  // 갱신된 좌표와 이동 횟수를 리턴
    }

    public int bfs(char[][] board, Node start) {  // start 지점에서 BFS를 수행하는 함수

        int n = board.length, m = board[0].length;  // 행과 열
        boolean[][] visited = new boolean[n][m];  // 방문 여부

        Queue<Node> q = new LinkedList<>();  // Node(좌표와 이동 횟수)를 가지는 큐 생성
        q.offer(start);
        visited[start.x][start.y] = true;

        while (!q.isEmpty()) {  // 큐가 빌 때까지 수행
            Node node = q.poll();

            for (int i = 0; i < 4; i++) {  // 상하좌우 반복

                Node newNode = slide(board, node, i);  // i 방향으로 슬라이딩 수행
                int nx = newNode.x, ny = newNode.y, nMove = newNode.move;

                if (board[nx][ny] == 'G')  // 목적지 도달 시, 이동 횟수 리턴
                    return nMove;

                if (!visited[nx][ny]) {  // 방문하지 않은 경우 큐에 삽입
                    q.offer(newNode);
                    visited[nx][ny] = true;
                }
            }
        }

        return -1;  // 목적지 도달 못한 경우, -1 리턴
    }

    public int solution(String[] board) {

        // String[] board 문자열 배열을 char[][] 2차원 문자 배열로 변환 (+ 시작 위치 저장)
        char[][] graph = new char[board.length][board[0].length()];
        Node start = null;

        for (int i = 0; i < board.length; i++)  {
            for (int j = 0; j < board[i].length(); j++) {
                graph[i][j] = board[i].charAt(j);
                if (graph[i][j] == 'R')
                    start = new Node(i, j, 0);
            }
        }

        // BFS 수행할 예정
        // 방문 처리 필요 (방문한 곳은 다시 방문하지 않음)
        // 횟수와 좌표를 큐에 담을 것임
        return bfs(graph, start);
    }
}