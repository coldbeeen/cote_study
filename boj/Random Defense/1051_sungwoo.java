// 풀이 시간: 18분
// 풀이 방법: 가능한 가장 큰 정사각형부터 시작해 크기가 2인 정사각형까지 줄여가며
//            꼭짓점이 모두 같은 정사각형을 찾음. 그때까지 안나온다면 1을 출력

import java.io.*;
import java.util.*;

public class Main
{
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력 받기
        String[] s = br.readLine().split(" ");
        int N = Integer.parseInt(s[0]), M = Integer.parseInt(s[1]);

        char[][] rect = new char[N][M];
        for (int i = 0; i < N; i ++) {
            rect[i] = br.readLine().toCharArray();
        }

        // 가능한 가장 큰 정사각형부터 탐색해나감
        for (int k = Math.min(N, M); - 1; k >= 1; k--) {  // k는 반대 꼭짓점을 계산하기 위한 값

            for (int i = 0; i + k < N; i++) {
                for (int j = 0; j + k < M; j++) {
                    if (rect[i][j] == rect[i][j + k] &&  // 4개의 꼭짓점이 모두 같다면 크기 출력 후 종료
                            rect[i][j + k] == rect[i + k][j] &&
                            rect[i + k][j] == rect[i + k][j + k]) {
                        System.out.println((int) Math.pow(k + 1, 2));
                        return;
                    }
                }
            }
        }

        System.out.println(1);
    }
}