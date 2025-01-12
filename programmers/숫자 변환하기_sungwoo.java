// 풀이 시간: 32분

import java.util.*;

class Solution {
    public int solution(int x, int y, int n) {

        int[] dp = new int[y + 1];  // DP 테이블 생성 (i로의 변환을 위한 최소 연산 횟수를 담음)
        Arrays.fill(dp, -1);  // -1로 채워 '변환 불가'를 기본값으로

        dp[x] = 0;  // x로의 변환은 0회로 설정한 뒤 반복문 시작

        for (int i = x + 1; i <= y; i++) {  // y로의 변환까지의 최소 연산 횟수를 DP로 계산

            int tmp = Integer.MAX_VALUE;

            // 3가지 경우의 수에 대해 '인덱스 유효성' 및 'num으로의 변환 가능 여부' 체크
            if (i - n >= x && dp[i - n] != -1)
                tmp = Math.min(tmp, dp[i - n] + 1);
            if (i % 2 == 0 && dp[i / 2] >= 0)
                tmp = Math.min(tmp, dp[i / 2] + 1);
            if (i % 3 == 0 && dp[i / 3] >= 0)
                tmp = Math.min(tmp, dp[i / 3] + 1);

            if (tmp != Integer.MAX_VALUE)  // 변환 가능하다면 dp 값 업데이트
                dp[i] = tmp;
        }

        return dp[y];
    }
}