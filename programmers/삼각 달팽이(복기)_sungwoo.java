// 풀이 시간: 31분

class Solution {
    public int[] solution(int n) {

        int[][] arr = new int[n][n];  // 2차원 삼각 달팽이 배열
        int num = n, i;  // num은 한 반복문(직선)의 반복 횟수(n, n-1, ..., 1)
        int x = 0, y = 0;  // 행 / 열 인덱스
        int cnt = 1;  // 배열에 넣을 숫자

        while (true) {

            for (i = 0; i < num; i++)  // 1. num만큼 아래로 채우기
                arr[x + i][y] = cnt++;
            x = x + i - 1; num--;  // 행과 num 업데이트
            if (num == 0) break;  // 더 이상 채울 필요 X


            for (i = 0; i < num; i++)  // 2. num만큼 오른쪽으로 채우기
                arr[x][y + i + 1] = cnt++;
            x--; y = y + i - 1; num--;  // 행과 열, num 업데이트
            if (num == 0) break;


            for (i = 0; i < num; i++)  // 3. num만큼 왼쪽 위 대각선으로 채우기
                arr[x - i][y - i] = cnt++;
            x = x - i + 2; y = y - i + 1; num--;  // 행과 열, num 업데이트
            if (num == 0) break;
        }

        int[] answer = new int[(n * (n + 1)) / 2];   // 정답 배열
        int answerIdx = 0;
        for (i = 0; i < n; i++)
            for (j = 0; j <= i; j++)
                answer[answerIdx++] = arr[i][j];

        return answer;
    }
}