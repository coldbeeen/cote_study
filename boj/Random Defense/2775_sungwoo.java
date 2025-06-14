// 풀이 시간: 12분
// 풀이 방법: 단순하게 생각하면 3중 반복문이 필요할 것 같지만, 아래층의 거주민을 계속 누적해나가며 값을 채워넣으면 된다.

import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int T = Integer.parseInt(br.readLine());

        int[][] arr = new int[15][15];
        for (int i = 0; i < 15; i++)
            arr[0][i] = i;

        for (int i = 1; i < 15; i++) {
            int sum = 0;
            for (int j = 0; j < 15; j++) {
                sum += arr[i-1][j];
                arr[i][j] = sum;
            }
        }

        for (int i = 0; i < T; i++) {
            int k = Integer.parseInt(br.readLine());
            int n = Integer.parseInt(br.readLine());
            System.out.println(arr[k][n]);
        }
    }
}