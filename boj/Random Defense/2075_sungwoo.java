// 풀이 시간: 23분
// 풀이 방법 1: 정렬 후 인덱싱 O(NlogN)
// 풀이 방법 2: 각 열의 행 인덱스 번호를 관리하며 N번 동안 최댓값을 반복하여 찾음 O(N)

import java.io.*;
import java.util.*;

public class Main
{
    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[][] arr = new int[N][N];  // 표 입력
        int[] rowIdx = new int[N];  // 각 컬럼의 행 인덱스 번호를 관리
        Arrays.fill(rowIdx, N - 1);  // 초기값은 N - 1

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++)
                arr[i][j] = Integer.parseInt(st.nextToken());
        }

        int k = 1;

        while (true) { // 최댓값을 N번 찾아 결과값을 출력 후 종료

            int max = arr[rowIdx[0]][0], maxIdx = 0;
            for (int j = 1; j < N; j++) {  // 각 열의 제일 아래 위치한 값들 중 최댓값을 찾음
                if (arr[rowIdx[j]][j] > max) {
                    max = arr[rowIdx[j]][j];
                    maxIdx = j;
                }
            }

            if (k == N) {  // N번째 최댓값을 출력 후 종료
                System.out.println(max);
                break;
            }

            rowIdx[maxIdx]--;  // 최댓값이 위치한 열의 행 인덱스 번호 감소
            k++;
        }
    }
}