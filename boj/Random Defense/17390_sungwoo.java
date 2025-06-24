// 풀이 시간: 18분

import java.io.*;
import java.util.*;

public class Main
{
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        // 1. N, Q 입력
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()), questionNum = Integer.parseInt(st.nextToken());

        // 2. 수열 입력 후 정렬
        st = new StringTokenizer(br.readLine());
        int[] arr = new int[N + 1];

        for (int i = 1; i <= N; i++)
            arr[i] = Integer.parseInt(st.nextToken());

        Arrays.sort(arr);

        // 3. 누적합을 계산
        for (int i = 1; i <= N; i++)
            arr[i] += arr[i - 1];

        // 4. L R 계산
        for (int i = 0; i < questionNum; i++) {
            st = new StringTokenizer(br.readLine());
            int l = Integer.parseInt(st.nextToken()), r = Integer.parseInt(st.nextToken());

            bw.write(arr[r] - arr[l - 1] + "\n");
        }
        bw.flush();
        bw.close();
    }
}