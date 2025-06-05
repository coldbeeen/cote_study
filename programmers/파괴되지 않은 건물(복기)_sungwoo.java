// 풀이 시간: 45분 - 누적합을 복구하는 방법 참고하였음 :(
// 풀이 방법: 누적합을 계산하는 방식으로 skill을 순회했고, 이후 누적합 배열을 복구해 결과를 구함
//         (차분 배열이라고 하는 것으로도 풀 수 있을 것 같다.)

class Solution {
    public int solution(int[][] board, int[][] skill) {

        int[][] prefixSum = new int[board.length][board[0].length];  // 누적합 배열

        for (int[] s: skill) {
            int degree = (s[0] == 1) ? s[5] : -s[5];
            int r1 = s[1], c1 = s[2], r2 = s[3], c2 = s[4];

            prefixSum[r2][c2] += degree;  // 누적합 방식으로 표시하기 위해 prefixSum을 업데이트
            if (c1 > 0) prefixSum[r2][c1 - 1] += -degree;
            if (r1 > 0) prefixSum[r1 - 1][c2] += -degree;
            if (c1 > 0 && r1 > 0) prefixSum[r1 - 1][c1 - 1] += degree;
        }

        // (이 부분을 떠올리지 못해 이전 코드 참고하였음)
        for (int j = board[0].length - 1; j >= 0; j--)  // 아래에서 위로 복구
            for (int i = board.length - 1; i > 0; i--)
                prefixSum[i - 1][j] += prefixSum[i][j];

        for (int i = board.length - 1; i >= 0; i--)  // 오른쪽에서 왼쪽으로 복구 (최종적으로 누적합 배열이 실제 배열로 복구됨)
            for (int j = board[0].length - 1; j > 0; j--)
                prefixSum[i][j - 1] += prefixSum[i][j];

        int answer = 0;
        for (int i = 0; i < board.length; i++)
            for (int j = 0; j < board[0].length; j++)
                if (board[i][j] - prefixSum[i][j] > 0)  // 공격을 받고 0보다 크다면 answer 증가
                    answer++;

        return answer;
    }
}