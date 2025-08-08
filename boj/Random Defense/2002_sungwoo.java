// 풀이 시간: 16분
// 풀이 방법: after를 끝까지 순회하면서 before와 비교해가며 추월한 차를 카운트 -> O(N)으로 해결

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {

        // 0. 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        final int N = Integer.parseInt(br.readLine());
        String[] before = new String[N];
        String[] after = new String[N];

        for (int i = 0; i < N; i++)
            before[i] = br.readLine();
        for (int i = 0; i < N; i++)
            after[i] = br.readLine();

        // 1. after를 끝까지 순회 (before와 비교해가며 추월한 차를 카운트)
        int result = 0, beforeIdx = 0, afterIdx = 0;  // result: 추월한 차 대수
        Set<String> set = new HashSet<>();  // 추월한 차는 before에서 건너뛸 수 있도록 set에 저장해 확인하도록 함

        while (afterIdx < N) {

            if (set.contains(before[beforeIdx])) {  // beforeIdx에 해당하는 차가 이미 추월했던 차인 경우 건너뜀 (순차적으로 O(1)으로 확인하기 위함)
                beforeIdx++;
                continue;
            }

            if (!before[beforeIdx].equals(after[afterIdx])) {  // 현재 before와 after의 차가 다르다면 afterIdx에 해당하는 차가 추월한 것!
                set.add(after[afterIdx]);  // Set에 추가하고 추월 카운트 증가 및 afterIdx 증가
                result++;
                afterIdx++;
            } else {  // 현재 before와 after의 차가 같다면 afterIdx에 해당하는 차는 추월하지 않은 차임
                beforeIdx++;
                afterIdx++;
            }
        }

        System.out.println(result);
    }
}

// 좋은 예시
// before: Z P R A B
// after:  P B A Z R