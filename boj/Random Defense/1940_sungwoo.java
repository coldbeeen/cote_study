// 풀이 시간: 9분
// 풀이 방법: 정렬하여 투 포인터를 사용해 조합을 찾아나간다.

import java.io.*;
import java.util.*;

public class Main
{
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];
        for (int i = 0; i < N; i++)
            arr[i] = Integer.parseInt(st.nextToken());

        // 배열 정렬
        Arrays.sort(arr);

        // 투 포인터를 활용해 조합을 찾아나감
        int result = 0, left = 0, right = N - 1;

        while (left < right) {

            int sum = arr[left] + arr[right];

            if (sum < M) {
                left++;
            } else if (sum > M) {
                right--;
            } else {
                result++;
                left++; right--;
            }
        }

        System.out.println(result);
    }
}