// 풀이 시간: 45분 (힌트: 문제 유형 참고)
// 풀이 방법: DP 테이블을 활용하여 풀이하였다.
//         현재까지 고려한 물건의 개수를 행으로, B 흔적 개수를 열로 두어 A 흔적 개수를 계산한다.
//         info를 순회하며 DP 테이블의 값을 차례로 (행별로) 갱신한다. (A 또는 B가 훔치는 두 가지의 경우의 수를 고려함)

import java.util.*;

class Solution {

    public final static int MAX = Integer.MAX_VALUE;

    public int solution(int[][] info, int n, int m) {

        int N = info.length;

        int[][] dp = new int[N + 1][m];  // DP 테이블 생성 및 상수 MAX로 초기화
        for (int i = 0; i < dp.length; i++)
            for (int j = 0; j < dp[i].length; j++)
                dp[i][j] = MAX;

        dp[0][0] = 0;

        for (int i = 0; i < N; i++) {  // info 순회 (dp 테이블의 행 순회이기도 함)

            int aMark = info[i][0], bMark = info[i][1];

            for (int j = 0; j < dp[i].length; j++) {

                if (dp[i][j] != MAX) {  // dp 값이 갱신되어 있는 대상에 대해 훔치기를 수행

                    // A가 훔칠 경우, aMark만 더하여 갱신
                    if (dp[i][j] + aMark < dp[i + 1][j])  // 최솟값을 넣기 위한 조건문
                        dp[i + 1][j] = dp[i][j] + aMark;

                    // B가 훔칠 경우, 열에 bMark를 더해 갱신
                    if (j + bMark < m && dp[i][j] < dp[i + 1][j + bMark])
                        dp[i + 1][j + bMark] = dp[i][j];

                }
            }
        }

        int min = Arrays.stream(dp[N]).min().getAsInt();

        return min < n ? min : -1;
    }
}