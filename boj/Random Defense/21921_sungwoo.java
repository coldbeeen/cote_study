// 풀이 시간: 16분
// 풀이 방법: 앞의 값을 빼고 뒤의 값을 더하는 방법으로 X개의 sum을 계속 업데이트하여 풀이함 (슬라이딩 윈도우)

import java.io.*;
import java.util.*;

public class Main
{
    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()), X = Integer.parseInt(st.nextToken()), sum = 0;
        int[] arr = new int[N];
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {  // 방문자 수 입력 받기
            arr[i] = Integer.parseInt(st.nextToken());

            if (i < X)  // 첫 X개의 sum 누적
                sum += arr[i];
        }

        int max = sum, maxCnt = 1;
        for (int i = 0; i < N - X; i++) {  // 앞의 값을 빼고 뒤의 값을 더하는 방법으로 X개의 sum을 계속 업데이트 (슬라이딩 윈도우)

            sum -= arr[i];
            sum += arr[i + X];

            if (sum > max) {  // max, maxCnt 업데이트
                max = sum;
                maxCnt = 1;
            } else if (sum == max) {  // maxCnt 업데이트
                maxCnt++;
            }
        }

        if (max == 0)
            System.out.println("SAD");
        else
            System.out.println(max + "\n" + maxCnt);
    }
}