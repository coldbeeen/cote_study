import java.io.*;
import java.util.*;

public class Main
{
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int D = Integer.parseInt(st.nextToken());

        ArrayList<int[]> shortcutList = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());

            shortcutList.add(new int[]{start, end, dist});
        }

        int[] dp = new int[D + 1];  // DP 배열 초기화
        for (int i = 0; i <= D; i++)  // 인덱스를 값으로 설정 (거리 초깃값 설정)
            dp[i] = i;

        for (int i = 0; i <= D; i++) {  // 위치(0 ~ D까지) 순회

            if (i > 0)  // 더 작은 값으로 거리를 이어나가도록 함
                dp[i] = Math.min(dp[i], dp[i - 1] + 1);

            for (int j = 0; j < N; j++) {  // 모든 지름길 순회  (시작 위치가 i일 때, dp[end] 값 갱신)
                int[] shortcut = shortcutList.get(j);
                int start = shortcut[0], end = shortcut[1], dist = shortcut[2];
                if (start == i && end <= D)
                    dp[end] = Math.min(dp[end], dp[i] + dist);
            }
        }

        System.out.println(dp[D]);
    }
}