// 풀이 방법: DFS로 자릿수를 하나씩 바꾸며 가능한 경우의 수 탐색
import java.io.*;
import java.util.*;

public class Main {
    private static int N, K, P, X;

    static int dfs(int[][] arr, int depth, int cnt, String sx) {
        if (depth == sx.length()) {  // base case
            int x = Integer.parseInt(sx);
            if (x == X) {  // 같은 층이면 카운트 X
                return 0;
            } else if (x >= 1 && x <= N) {  // 같은 층이 아니고 1 <= x <= N이라면 카운트 대상
                return 1;
            } else {
                return 0;
            }
        }

        int result = 0;
        int cur = sx.charAt(depth) - '0';  // 현재 숫자

        for (int i = 0; i < 10; i++) {  // sx의 depth번 인덱스의 숫자를 i로 교체하여(dx) dfs 재귀
            if (cur != i && arr[cur][i] <= cnt) {
                String dx = sx.substring(0, depth) + i + sx.substring(depth + 1);
                result += dfs(arr, depth + 1, cnt - arr[cur][i], dx);
            } else if (cur == i) {  // 같은 숫자인 경우 그대로 dfs 재귀
                result += dfs(arr, depth + 1, cnt, sx);
            }
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        N = Integer.parseInt(s[0]);
        K = Integer.parseInt(s[1]);
        P = Integer.parseInt(s[2]);
        X = Integer.parseInt(s[3]);

        String sx = String.valueOf(X);
        if (sx.length() < K) {
            sx = "0".repeat(K - sx.length()) + sx;  // 앞자리 0으로 채우기
        }

        String[] num = {  // 7개의 LED를 String으로 표현 (시계 방향)
            "1111110", "0110000", "1101101", "1111001", "0110011",  // 0, 1, 2, 3, 4
            "1011011", "1011111", "1110000", "1111111", "1111011"  // 5, 6, 7, 8, 9
        };

        int[][] arr = new int[10][10];
        for (int i = 0; i < 10; i++) {  // i를 j로 만드는 데에 몇 번의 반전이 필요한지 계산
            for (int j = 0; j < 10; j++) {
                if (i != j) {
                    int d = 0;
                    for (int h = 0; h < 7; h++) {
                        if (num[i].charAt(h) != num[j].charAt(h)) {
                            d++;
                        }
                    }
                    arr[i][j] = d;
                }
            }
        }

        System.out.println(dfs(arr, 0, P, sx));
    }
}
