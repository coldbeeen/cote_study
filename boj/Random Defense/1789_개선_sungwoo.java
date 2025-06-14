// 풀이 시간: 6분
// 풀이 방법: 이분 탐색은 log(S)로 훨씬 빠를 것이므로 구현해보았음

import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long s = Long.parseLong(br.readLine());

        long start = 1, end = s;  // 1과 s 사이에 존재

        while (start <= end) {  // 이분 탐색 수행

            long mid = (start + end) / 2;  // mid 계산 후
            long sum = (mid * (mid + 1)) / 2;  // 시그마 공식으로 합을 구함

            if (sum <= s)  // 앞 구간 탐색 (최종 출력은 end이므로 s와 같은 경우도 이 분기에 포함)
                start = mid + 1;
            else // 뒷 구간 탐색
                end = mid - 1;
        }

        System.out.println(end);
    }
}