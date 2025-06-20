// 풀이 시간: 35분
// 풀이 방법: 백트래킹 방식으로 가능한 경우의 수를 탐색하며 해를 구한다.

import java.io.*;
import java.util.*;

public class Main {

    public static int N, result;  // 남은 일수와 최대 수익

    public static void getMaxEarning(int[] durationArr, int[] earningArr, int curr, int earningSum) {  // 백트래킹 함수

        if (curr + 1 <= N)  // 이번 상담을 건너뜀
            getMaxEarning(durationArr, earningArr, curr + 1, earningSum);

        if (curr < N && curr + durationArr[curr] <= N)  // 이번 상담을 수행 (curr와 priceSum에 대해 상담 기간 및 비용을 더함)
            getMaxEarning(durationArr, earningArr, curr + durationArr[curr], earningSum + earningArr[curr]);

        result = Math.max(result, earningSum);  // earningSum의 최댓값을 갱신
    }

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        int[] durationArr = new int[N];
        int[] earningArr = new int[N];

        for (int i = 0; i < N; i++) {
            String[] s = br.readLine().split(" ");
            durationArr[i] = Integer.parseInt(s[0]);
            earningArr[i] = Integer.parseInt(s[1]);
        }

        getMaxEarning(durationArr, earningArr, 0, 0);  // 인덱스 0, 금액 0으로 백트래킹 탐색을 수행함
        System.out.println(result);
    }
}