// 풀이 시간: 40분 시도 후 레퍼런스 참고
// A도둑이 남긴 흔적이 n보다 작아야 하고 B도둑이 남긴 흔적이 m보다 작아야 한다. 
// 그래서 행을 훔친 물건의 개수로 잡고 열의 최대 크기를 m-1로 잡는다.
// b의 흔적 개수 0 <= 흔적 개수 < m 즉, b가 허용 가능한 흔적 개수를 for문을 돌면서 선택을 한다. 

import java.util.*;

class Solution {

    static final int MAX = 120;

    public int solution(int[][] info, int n, int m) {

        int[][] dp = new int[info.length + 1][m];  // DP 테이블 생성 (행은 고려한 info의 개수, 열은 B의 흔적 개수)

        for (int i = 0; i < info.length + 1; i++)  // DP 테이블 초기화
            Arrays.fill(dp[i], MAX);

        dp[0][0] = 0;

        for (int i = 1; i <= info.length; i++) {

            int a = info[i - 1][0], b = info[i - 1][1];  // A의 흔적, B의 흔적

            for(int j = 0; j < m; j++){
                // A가 훔친다 - B의 흔적 개수(j)는 그대로, A의 흔적 개수는 a만큼 늘려줌
                dp[i][j] = Math.min(dp[i][j], dp[i-1][j] + a);

                // B가 훔친다 - B의 흔적 개수(j)를 b만큼 늘리고, A의 흔적 개수는 그대로
                if(j + b < m){
                    dp[i][j + b] = Math.min(dp[i][j + b], dp[i-1][j]);
                }
            }
        }


        // dp의 모든 열은 가능한 허용 범위인 m 이내의 값만 기록하였기 때문에 A의 흔적 개수 min값만 갱신하면 됨
        int min = MAX;
        for(int j = 0; j < m; j++)
            min = Math.min(min, dp[info.length][j]);

        return min >= n ? -1 : min;
    }
}