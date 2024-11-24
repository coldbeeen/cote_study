// 풀이 시간: 38분
// 규칙 찾아내서 풀려고 했으나 간단치 않아 직접 배열 생성함

import java.util.*;

class Solution {
    public int[] solution(int n) {

        int[][] arr = new int[n][n];  // 삼각 달팽이 배열
        int i = 0, j = 0, cnt = 1;  // cnt는 배열에 넣을 수

        for (int iter = 0; iter < n; iter++) {  // 배열 채우는 과정을 n번 수행
            if (iter % 3 == 0) {
                while (i < n - (iter / 3))  // 아래로 채우기
                    arr[i++][j] = cnt++;
                i--; j++;  // 인덱스 조정
            }
            else if (iter % 3 == 1) {
                while (j < n - (iter / 3) * 2)  // 오른쪽으로 채우기
                    arr[i][j++] = cnt++;
                i--; j -= 2;  // 인덱스 조정
            }
            else {
                while (i > (iter / 3) * 2)  // 왼쪽 위로 채우기
                    arr[i--][j--] = cnt++;
                i += 2; j++;  // 인덱스 조정
            }
        }

        int[] answer = new int[(n * (n + 1)) / 2];  // 정답 배열
        int answerIdx;

        for (i = 0; i < n; i++)
            for (j = 0; j < i + 1; j++)
                answer[answerIdx++] = arr[i][j];  // answer 채우기

        return answer;
    }
}