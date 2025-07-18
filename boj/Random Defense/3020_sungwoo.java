// 풀이 시간: 41분
// 풀이 방법: 석순과 종유석에 대해 각각 Prefix Sum을 만들어 계산 후 최솟값을 구함

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int N = Integer.parseInt(s[0]), H = Integer.parseInt(s[1]);
        int[] obstacle = new int[N];

        for (int i = 0; i < N; i++) {
            obstacle[i] = Integer.parseInt(br.readLine());
        }

        int[] up = new int[H];  // 석순 (DP 배열)
        int[] down = new int[H];  // 종유석 (DP 배열)

        for (int i = 0; i < N; i++) {  // Prefix Sum 계산을 위해, 장애물 위치 기반으로 1을 더해 표시

            if (i % 2 == 0)
                ++up[obstacle[i] - 1];
            else
                ++down[H - obstacle[i]];
        }

        for (int i = H - 1; i > 0; i--)  // 석순 Prefix Sum 계산
            up[i - 1] += up[i];

        for (int i = 0; i < H - 1; i++)  // 종유석 Prefix Sum 계산
            down[i + 1] += down[i];

        int min = Integer.MAX_VALUE, minCnt = 0;

        for (int i = 0; i < H; i++) {  // Prefix Sum 기반으로 i 구간에서 파괴해야할 장애물 계산 및 최솟값 갱신

            int toDestroy = up[i] + down[i];

            if (toDestroy < min) {
                min = toDestroy;
                minCnt = 1;
            } else if (toDestroy == min) {
                minCnt++;
            }
        }

        System.out.println(min + " " + minCnt);
    }
}d