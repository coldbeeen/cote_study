// 구글링

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] dp = new int[N + 1];
        for (int i = 1; i <= N; i++) {  // i를 만들기 위한 최솟값을 찾아나감
            dp[i] = arr[i];
            for (int j = 1; j < i; j++) {  // **i보다 작은 값의 조합으로 최솟값이 되는지 확인**
                dp[i] = Math.min(dp[i], dp[j] + dp[i - j]);
            }
        }

        System.out.println(dp[N]);
    }
}