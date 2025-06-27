// 풀이 시간: 30분
// 풀이 방법: DP. 규칙을 찾아서 적용함.
//           해설을 읽어보니 새로운 2 X 1 우리를 추가할 때 아래를 고려해 점화식이 만들어진다고 한다.
//           1. 사자를 배치 안하는 경우의 수 (dp[i-1])
//           2. 사자를 배치 하는 경우의 수 (dp[i-2] + (dp[i-1] - dp[i-2]) / 2) * 2

import java.io.*;
import java.util.*;

public class Main
{
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int N = Integer.parseInt(br.readLine());

        long[] dp = new long[N + 1];
        dp[0] = 1;
        dp[1] = 3;

        for (int i = 2; i <= N; i++) {
            dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901;
        }

        System.out.println(dp[N]);
    }
}