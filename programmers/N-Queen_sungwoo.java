import java.util.*;

class Solution {

    int answer = 0;
    boolean[] v1, v2, v3;  // v1은 열 확인용, v2와 v3는 대각선 확인용 boolean 배열

    public void dfs(int row, int n) {  // DFS 탐색 (백트래킹)
        if (row == n) {
            answer += 1;  // row가 n과 같아지면 조건을 만족하는 배치이므로 answer 증가
        } else {
            for (int i = 0; i < n; i++) {  // n개의 열에 대한 순회
                if (v1[i] || v2[row + i] || v3[n + row - i])  // 열과 대각선에 대한 검증 (boolean 배열 활용)
                    continue;
                v1[i] = v2[row + i] = v3[n + row - i] = true;  // i에 놓았음을 boolean 배열에 표시
                dfs(row + 1, n);  // 다음 행에 대해 이어서 탐색
                v1[i] = v2[row + i] = v3[n + row - i] = false;  // boolean 배열 원상복구
            }
        }
    }

    public int solution(int n) {
        v1 = new boolean[n];
        v2 = new boolean[n*2];
        v3 = new boolean[n*2];
        dfs(0, n);
        return answer;
    }
}